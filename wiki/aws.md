# Backing up files to AWS

## After installing the aws cli
`aws configure`
Then enter the items below
~~~
AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: us-east-1
Default output format: json
~~~
# Verify it works
`aws sts get-caller-identity`
# List all S3 buckets
`aws s3 ls`

## Encrypt before backup ##
`gpg --symmetric --cipher-algo AES256 myfile.txt`
Prompts for a passphrase — produces myfile.txt.gpg

## Copy files to S3 Glacier class storage ##
aws s3 cp myfile.txt s3://your-bucket-name/ \
  --storage-class GLACIER

## Tar commands
The - after the -cvf is to send the stream to stdout so it can get to split
`tar -cvf - /path/to/large_folder | split -b 20G - backup_part_`

-c: Creates a new archive

-v: Verbose mode (lists the files as they are being processed so you can see the progress)

-f -: Tells tar to send the output directly to stdout (the screen/pipe) instead of writing a single massive file to disk

| (The Pipe): Takes that data stream and hands it straight to the split command
split -b 20G - backup_part_:

-b 20G: Splits the incoming data into 20 GiB pieces

-: Tells split to read from stdin (the data coming from the pipe)

backup_part_: The prefix for your output files. Your final directory will fill up with files named backup_part_aa, backup_part_ab, backup_part_ac, and so on.`

Stitch files back together
`cat backup_part_* | tar -xvf -`

Issues with errors - use this for logging
`tar -cvf - /path/to/large_folder 2> tar_errors.log | split -b 20G - backup_part_`
## Viewing files in a tarball
tar -tf archive.tar
### Create log file with list of files in the tarball (bash)
Some errors about EOF are generated but it works
`for f in *.tar; do tar -tf "$f" > "${f%.tar}.log"; done`
## Testing the tarball
`tar -tf test.tar &> /dev/null; echo $?`
tar — the tar command

-tf — two flags combined:

-t — list contents of the archive

-f — the next argument is the filename

test.tar — the tarball to inspect

&> — redirect both stdout and stderr to the same place:

> alone only redirects stdout
2> alone only redirects stderr
&> redirects both at once (bash shorthand for 2>&1 >)

/dev/null — a black hole that discards everything written to it. The tar output is thrown away — we only care whether it succeeded or failed.
; — run the next command sequentially, regardless of whether the first command succeeded or failed (unlike && which only runs the next command if the first succeeded)
echo $? — prints the exit code of the last command:

0 = success (valid tar archive)
non-zero = failure (corrupt, wrong format, missing file, etc.)
