"""
find_duplicates.py
------------------
This script scans a folder (and all its subfolders) for duplicate files.
It uses an MD5 hash to identify files with identical content, then writes
the results to a CSV file so you can easily review them.

HOW IT WORKS (two-pass approach):
  Pass 1 — Walk every file and record its MD5 hash. Only the hash and path
            are kept in memory — no file details. This lets us identify which
            hashes appear more than once (i.e. duplicates) without storing
            everything.
  Pass 2 — Walk the files again. This time, any file whose hash was seen more
            than once gets written to the CSV immediately, row by row. Memory
            stays low and the file grows in real time.

HOW TO USE:
  1. Set the FOLDER_TO_SCAN variable to the folder you want to check.
  2. Set the OUTPUT_CSV variable to where you want the results saved.
  3. Run the script:  python find_duplicates.py
"""

import os       # For walking through folders and building file paths
import hashlib  # For generating MD5 hashes to compare file contents
import csv      # For writing the results to a CSV file
import datetime # For converting file timestamps into readable dates


# ──────────────────────────────────────────────
# SETTINGS  ← Change these two lines as needed
# ──────────────────────────────────────────────

FOLDER_TO_SCAN = "/run/user/1000/gvfs/smb-share:server=synology123.local,share=pics/Pics/" # The folder you want to scan
OUTPUT_CSV     = "/home/ajay/duplicate_files.csv"  # The CSV file that will be created


# ──────────────────────────────────────────────
# HELPER: Calculate an MD5 hash for a file
# ──────────────────────────────────────────────

def get_md5_hash(file_path):
    """
    Reads a file in small chunks and builds an MD5 hash string.
    Files with identical content will always produce the same hash.
    Returns the hash as a hex string (e.g. 'd41d8cd98f00b204e9800998ecf8427e').
    Returns None if the file could not be read (e.g. permission error).
    """
    hasher = hashlib.md5()

    try:
        with open(file_path, "rb") as f:
            # Read 64 KB at a time to avoid loading huge files into memory
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()

    except (OSError, PermissionError) as error:
        print(f"  [WARNING] Could not read file: {file_path}\n  Reason: {error}")
        return None


# ──────────────────────────────────────────────
# HELPER: Get human-readable file size
# ──────────────────────────────────────────────

def get_file_size(size_bytes):
    """
    Converts a raw byte count into a readable string like '3.45 MB'.
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.2f} MB"
    else:
        return f"{size_bytes / 1024 ** 3:.2f} GB"


# ──────────────────────────────────────────────
# HELPER: Get formatted file creation time
# ──────────────────────────────────────────────

def get_created_time(stat):
    """
    Returns the file creation time as a formatted string 'YYYY-MM-DD HH:MM:SS'.
    Uses st_birthtime on Mac/Windows (true creation time), falls back to
    st_ctime on Linux (closest available approximation).
    """
    raw_timestamp = getattr(stat, "st_birthtime", stat.st_ctime)
    return datetime.datetime.fromtimestamp(raw_timestamp).strftime("%Y-%m-%d %H:%M:%S")


# ──────────────────────────────────────────────
# PASS 1: Build a set of duplicate MD5 hashes
# Only hashes + paths are stored — nothing else.
# ──────────────────────────────────────────────

def build_hash_index(folder):
    """
    Walks every file in the folder tree and maps each MD5 hash to a list
    of file paths that share that hash.

    Returns a SET of MD5 hashes that appear more than once (duplicates).

    Memory use is minimal because we only store the hash string and file
    path — no filenames, sizes, timestamps, or other metadata.
    """
    hash_index = {}  # { md5_string: count_of_files_seen }
    total = 0

    print(f"\nPass 1 of 2 — Hashing files in: {os.path.abspath(folder)}")
    print("-" * 50)

    for current_folder, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            full_path = os.path.join(current_folder, filename)
            total += 1
            print(f"  Hashing ({total}): {full_path}")

            md5 = get_md5_hash(full_path)

            if md5 is None:
                continue  # Skip unreadable files

            # Count how many times we've seen this hash
            if md5 not in hash_index:
                hash_index[md5] = 0
            hash_index[md5] += 1

    print(f"\n  Total files scanned: {total}")

    # Return only the hashes seen more than once — these are the duplicates
    duplicate_hashes = {md5 for md5, count in hash_index.items() if count > 1}
    print(f"  Duplicate hashes found: {len(duplicate_hashes)}")

    return duplicate_hashes


# ──────────────────────────────────────────────
# PASS 2: Walk again, stream duplicates to CSV
# ──────────────────────────────────────────────

def stream_duplicates_to_csv(folder, duplicate_hashes, output_path):
    """
    Walks the folder tree a second time. For each file whose MD5 is in
    duplicate_hashes, its details are written to the CSV immediately —
    one row at a time. The CSV file stays open throughout so nothing is
    held in memory waiting to be flushed at the end.

    csv_file.flush() is called after every row, which pushes the data to
    disk right away rather than buffering it — so the file grows in real
    time and progress is never lost if the script is interrupted.

    A 'group number' is assigned per unique hash so duplicates are
    visually grouped in the output. Blank rows separate each group.
    """
    if not duplicate_hashes:
        print("\n  No duplicates to write. CSV will not be created.")
        return 0

    # Assign a stable group number to each duplicate hash.
    # Sorting ensures the group order is consistent between runs.
    group_map = {md5: i + 1 for i, md5 in enumerate(sorted(duplicate_hashes))}

    # Track the last group written so we know when to insert a blank separator
    last_group_written = None
    total_rows_written = 0

    print(f"\nPass 2 of 2 — Writing duplicates to: {os.path.abspath(output_path)}")
    print("-" * 50)

    # Open the CSV once and keep it open for the entire second pass
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row and flush it to disk immediately
        writer.writerow(["Group", "Filename", "Full Path", "MD5 Hash", "File Size", "Created"])
        csv_file.flush()

        for current_folder, subfolders, filenames in os.walk(folder):
            # Sort filenames so files in the same group appear together
            for filename in sorted(filenames):
                full_path = os.path.join(current_folder, filename)

                md5 = get_md5_hash(full_path)

                # Skip files that aren't duplicates or couldn't be read
                if md5 is None or md5 not in duplicate_hashes:
                    continue

                # Get file metadata
                try:
                    stat = os.stat(full_path)
                    size_str    = get_file_size(stat.st_size)
                    created_str = get_created_time(stat)
                except (OSError, PermissionError) as error:
                    print(f"  [WARNING] Could not read metadata: {full_path}\n  Reason: {error}")
                    size_str    = "ERROR"
                    created_str = "ERROR"

                group_number = group_map[md5]

                # Insert a blank separator row whenever the group changes
                if last_group_written is not None and group_number != last_group_written:
                    writer.writerow(["", "", "", "", "", ""])
                    csv_file.flush()

                # Write this file's row immediately to the CSV
                writer.writerow([
                    group_number,
                    filename,
                    full_path,
                    md5,
                    size_str,
                    created_str,
                ])

                # Flush pushes the row to disk right now instead of buffering it
                csv_file.flush()

                last_group_written = group_number
                total_rows_written += 1
                print(f"  Written (group {group_number}): {full_path}")

    return total_rows_written


# ──────────────────────────────────────────────
# MAIN: Tie the two passes together
# ──────────────────────────────────────────────

def main():
    # Check the target folder actually exists before we start
    if not os.path.isdir(FOLDER_TO_SCAN):
        print(f"\n[ERROR] Folder not found: '{FOLDER_TO_SCAN}'")
        print("Please update the FOLDER_TO_SCAN variable at the top of this script.")
        return

    # Pass 1: Hash every file and find which hashes are duplicates
    duplicate_hashes = build_hash_index(FOLDER_TO_SCAN)

    # Pass 2: Walk again and stream duplicate rows straight to the CSV
    rows_written = stream_duplicates_to_csv(FOLDER_TO_SCAN, duplicate_hashes, OUTPUT_CSV)

    # Final summary
    print(f"\nTotal duplicate rows written: {rows_written}")
    if rows_written > 0:
        print(f"Results saved to: {os.path.abspath(OUTPUT_CSV)}")
    print("\nDone!")


# This makes sure main() only runs when you execute this file directly,
# not when another script imports it.
if __name__ == "__main__":
    main()