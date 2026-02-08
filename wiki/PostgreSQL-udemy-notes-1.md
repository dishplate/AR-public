```
Tables contain columns and rows or fields and rows

Data types
INT or integer. Used to store whole numbers, eg. Age or quantity
NUMERIC(P,S) decimal numbers. for 4.33 the P is the max digits so the P is 3. The S is the number of digits after the decimal point, 2.
SERIAL - it auto increments whole numbers, used for primary key or ID columns
CHAR(N) - strings of fixed length, N is the length, eg. M for male or F for female
VARCHAR(N) - strings of varying length of max length N, eg, email or name
TEXT - varying length with no maximum, eg. Comments or reviews
TIME - HH:MM:SS
DATE - YYYY-MM-DD, eg. date of birth
TIMESTAMP - YYYY-MM-DD HH:MM:SS eg. order time 
BOOLEAN - true or false, eg. in stock or not
ENUM - A list of values input by the user, eg. Gender


PRIMARY KEYS
A column which uniquely identifies a record in a table.
Must be unique and cannot be null.
Only 1 per table, not compulsory but highly recommended.

FOREIGN KEY
Is used to link two tables together
A foreign key is a column where the values match the values of ANOTHER table's PRIMARY key column.
The table with the primary key is called the reference, or parent, table and the table wit the
foreign key is called the child table.
A table can have multiple foreign tables.

Unique constraint
Ensures that a column can only contain unique values.
Throws an error if duplicate values are inserted into a column.
You can state whether a column should have a unique constraint when creating the table.
eg. email address column

NOT NULL CONSTRAINT
Ensures that NULL values can not be inserted into a column.
If the data is vital then you can add the NOT NULL constraint.
Define a column with the NOT NULL constraint when creating the table.

CHECK CONSTRAINT
Used to check whether values in a columns satisfy a specific boolean.
Eg. Age column must contain values greater than zero.

Creating your first table
In pgadmin, right click and create a new database. It is customary to use underscore instead of spaces.
Then right click on the database and choose CREATE SCRIPT. Add your code below any existing code.
The -- is how comments are made in PSQL (and SQL?)
A table is created along with columns, note the data types and the limits on the column lengths.

-- create the directors table
CREATE TABLE directors (

	directors_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	date_of_birth DATE,
	nationality VARCHAR(20)

);

CREATE TABLE actors (
	actor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	gender CHAR(1),
	date_of_birth DATE
	
);

SELECT * FROM actors;


```
# Udemy Course: SQL and PostgreSQL: The Complete Developer's Guide

Setup PostgreSQL docker

Download and install pgadmin4 for MacOS. Setting up pgadmin4 for Ubuntu on ARM doesn't work.

On the system with docker
	Docker Hub: https://hub.docker.com/_/postgres/
	docker pull postgress
	docker run --name postgres_container -e POSTGRES_PASSWORD=some-password -d -p 5432:5432 postgres
	Once installed, use nmap to check that the MacOS can see the VM running docker and the postgres port
	nmap -p 5432 10.x.x.x
	Open pgadmin4 and connect to the ip with default username postgress and the password you set above in the docker run command.


