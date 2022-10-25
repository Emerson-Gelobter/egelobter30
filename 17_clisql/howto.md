Timmy, Dini, and Bob's Adventures: Samantha Hua, Anjini Katari, Emerson Gelobter
SoftDev
K17: Shell Game
2022-10-24
time spent: 1.0hrs

Notes:
 * All SQLite Shell commands begin with a .
 * When you write SQL operations, you need a semicolon at the end
      ex: CREATE TABLE bloop (name TEXT, id INTEGER PRIMARY KEY)
 * You have to open a database before you can do anything inside it


 |Command|What it does|
 |-------|------------|
 | .show | showed the stats of your database including what settings you have on|
 | .exit | exited the SQLite shell|
 | .help | prints out all of the commands you can run in the shell|
 | .header on/off | turns on the header setting on off (we think this will change how the query treats the first row of the db)|\
 | .open FILENAME | allows you to manipulate and access a specific database|

 |Operation|What it does|
 |---------|------------|
 |select * from DBNAME| prints all of the contents in the database|
 | create table TABLENAME(one COLUMNNAME, two COLUMNNAME, etc) | creates a new table with the specified columns|
 | insert into TABLENAME values(...) | inserts a new line of data into the database|
