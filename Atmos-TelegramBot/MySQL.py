# Using the mysqlpy package in pip

import mysql.connector
from mysql.connector import errorcode
from Utils import sprint


host = '127.0.0.1'
def getConnection(user, password, database):
    try:
        return mysql.connector.connect(user=user, password=password,
                                database=database)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            sprint("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            sprint("Database does not exist")
        else:
            sprint(err)


def run(connection, comm):
    cursor = connection.cursor()
    try:
        cursor.execute(comm)
        return cursor
    except mysql.connector.Error as err:
        sprint("Error running statement: {}".format(err))
        exit(1)


def create_database(cnx, db):
    cursor = cnx.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
    except mysql.connector.Error as err:
        sprint("Failed creating database: {}".format(err))
        exit(1)


def changeDB(cnx, db):
    cursor = cnx.cursor()
    try:
        cnx.database = db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db)
            cnx.database = db
        else:
            sprint(err)
            exit(1)
