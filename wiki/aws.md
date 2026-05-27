# AWS notes

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
