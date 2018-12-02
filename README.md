# flaskCRUD
Following a tutorial to create a full CRUD application using flask. 


## Init setup

- Created folder structure
- Added CI integration using CircleCi
- Using virtualenv, named: env
- Going to be using flake8 to check code linting
- using pytest to run unit tests

## Setting up the db

- connecting (After setting up the db - installing and setting path variables)
  - Use the following to connect: mysql -u root -p
- Create a user, for the purpose of this example, using the following:
```SQL
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
```
- Create the database, using:
```SQL
CREATE DATABASE dreamteam_db;
```
- Grant privileges to the db with the user we just created:
```SQL
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';
```
- After which we setup the config.py file to work with the db
- After the generic config file, we setup an instance config file - this is used to hold sensitive data (that we don't want to push to version control)
  - Which means, don't forget to add to your .gitignore file

