-- Script to list all the tables of a database

USE mysql;

set @dbname = '$database_name';

SELECT table_name FROM information_schema.tables WHERE table_schema = @dbname;
