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
~~~
-c: Creates a new archive.
-v: Verbose mode (lists the files as they are being processed so you can see the progress).
-f -: Tells tar to send the output directly to stdout (the screen/pipe) instead of writing a single massive file to disk.
| (The Pipe): Takes that data stream and hands it straight to the split command.
split -b 20G - backup_part_:
-b 20G: Splits the incoming data into 20 GiB pieces.
-: Tells split to read from stdin (the data coming from the pipe).
backup_part_: The prefix for your output files. Your final directory will fill up with files named backup_part_aa, backup_part_ab, backup_part_ac, and so on.`
~~~
Stitch files back together
`cat backup_part_* | tar -xvf -`

Issues with errors - use this for logging
`tar -cvf - /path/to/large_folder 2> tar_errors.log | split -b 20G - backup_part_`
## Viewing files in a tarball
tar -tf archive.tar
