```
For Ubuntu or its variants
https://www.youtube.com/watch?v=tducLYZzElo
Follow instructions: https://www.postgresql.org/download/linux/ubuntu/

Get the adventureworks demo data from Microsoft but use all instructions from here:
https://github.com/lorint/AdventureWorks-for-Postgres?tab=readme-ov-file
The instructions are not the clearest but get the files from the repo and use nano or vi to make and save the scripts in a file that is accessible by the postgres user, as created from the video.

First query

SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND
    schemaname != 'information_schema';
```