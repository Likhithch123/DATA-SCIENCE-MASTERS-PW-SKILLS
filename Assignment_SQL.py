'''
1A: A database is an organised way of collecting and storing the         information
    in a database management system. The data in common databases is
    modeled in tables, making querying and processing efficient. Struc
    tured Query Language is commonly used for data querying and writing. It is a process of storing and retrieving data efficiently from the database and its very easy since it involves operations in the form of queries.

    Coming to the differences between sql and nosql databases are:
    * SQL allows only structured data wheres as NOSQL allows unstructured data
    * few common examples of sql are: MySQL,PostgreSQL,Oracle,MS-SQL.
    * few common examples of nosql are: MongoDb,HBase,Neo4j,Cassandra.
'''

'''
    2A: DDL stands for Data Definition Language. It is a subset of sql. 
        It is a language for describing data and its relationship in DBase. We specify a DB schema by a set of defintions expressed 
        by a special language called as Data Definition Language.

        1) Create: It is used for creating a new tables in the database.
        2) Alter: This command has many features like adding a column into the existing database or modifying a column name in the table and in some cases alter is used for renaming and deleting the tables in the database also.
        3) Truncate: This command is used for deleting all the rows/data in the table but the table still exists in the database.
        4) Drop: This command is used for deleting the table from the database.

        ** lets see the use of all commands below:
'''

'''
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='abc',password='password')
cur=conn.cursor()
cur.execute('create database if not exists database_1')
cur.execute('use database_1')
cur.execute('create table if not exists table_1(std_id int,std_name varchar(20),std_batch varchar(20))')
cur.execute('alter table table_1 add(platform varchar(20))')
cur.execute('insert into table_1 values(100,"likhith","Data Science Masters","PW SKILLS")')
conn.commit()
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.execute('truncate table table_1')
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.execute('drop table table_1')
cur.execute('show tables')
for item in cur.fetchall():
    print(item)
conn.close()

'''

'''
    3A: DML stands for Data Manipulation Language, is a language that enables users to access or manipulate data as organised by appropriate data model.

    1) Insert: This command is used for inserting the data into the tables.
    2) Update: This command is used to change/modify the data at a specified position in the table.
    3) Delete: This command is used to delete the selected rows from the relation/table.
'''

''' 

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='abc',password='password')
cur=conn.cursor()
cur.execute('use database_1')
cur.execute('create table if not exists table_1(std_id int,std_name varchar(20),std_batch varchar(20))')
cur.execute('insert into table_1 values(100,"likhith","Data Science Masters")')
conn.commit()
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.execute('update table_1 set std_id=105 where std_name="likhith" ')
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.execute('delete from table_1 where std_id=105')
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.close()
conn.close()

'''

'''
    4A: DQL stands for Data Query Language which includes select command.

    1) Select command displays the no.of columns from the table which are specified in the query .
    * If we specify * after select we get all the fields of the table.
'''

''' 

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='abc',password='password')
cur=conn.cursor()
cur.execute('use database_1')
cur.execute('insert into table_1 values(100,"likhith","Data Science Masters")')
conn.commit()
cur.execute('select * from table_1')
for item in cur.fetchall():
    print(item)
cur.close()
conn.close()

'''

'''
    5A: 
    Primary key: A primary key is used to ensure data in the specific column is unique. It uniquely identifies a record in the relational database table. Only one primary key is allowed in a table. It does not allow NULL values. Its value cannot be deleted from the parent table.

    Foreign key: A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables. It refers to the field in a table which is the primary key of another table. Whereas more than one foreign key is allowed in a table. It can also contain NULL values. Its value can be deleted from the child table.
'''

''' 
    6A: 
    cursor() creates a pointer in python in order to point to a database and do all our required work using that single cursor we created for the database.

    Execute(): It is method which accepts the queries from us and performs specified on the data base.

'''

'''

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='abc',password='password')
cur=conn.cursor()
cur.execute('show databases')
for item in cur.fetchall():
    print(item)
cur.close()
conn.close()

'''


'''
    7A:
    FROM: This clause specifies the table from which the data will be retrieved.

    WHERE: This clause filters the rows based on a specified condition.

    GROUP BY: If used, this clause groups the result set by one or more columns.

    HAVING: Similar to the WHERE clause but used with aggregated functions when using GROUP BY.

    SELECT: This clause selects the columns to be displayed in the result set.

    ORDER BY: This clause sorts the result set based on the specified columns and order (ascending or descending).

    LIMIT / OFFSET: If used, these clauses limit the number of rows returned and provide a way to paginate through the result set.
'''