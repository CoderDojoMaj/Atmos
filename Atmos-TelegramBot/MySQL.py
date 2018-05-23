# Using the mysqlpy package in pip

import mysql.connector
from mysql.connector import errorcode
from time import strftime, localtime
from Utils import sprint


host = '127.0.0.1'
def getConnection(user, password, database):
    try:
        r = mysql.connector.connect(user=user, password=password, database=database, host = '127.0.0.1',port='3306')
        c = r.cursor()
        c.close()
        if r is None:
            sprint('Couldn\'t connect to the database')
            exit(1)
        return r

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            sprint("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            sprint("Database does not exist")
        else:
            sprint(err)
        exit(1)


def run(connection, comm):
    cursor = None
    sprint(comm)
    try:
        cursor = connection.cursor()
    except mysql.connector.errors.OperationalError:
        connection.reconnect()
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

def addMeteoData(connection, temp, hum, luz, pres):
    # timestamp = strftime('%d-%m-%Y %H:%M:%S', localtime())
    statement = 'INSERT INTO MeteoData(fecha, temp, hum, luz, pres) VALUES(NOW(), {}, {}, {}, {});'.format(
        temp, hum, luz, pres)
    sprint(temp, hum, luz, pres)
    run(connection, statement)

def getLastLecture(connection):
    statement = "select temp as tempf,hum as humf,luz as ligf,pres as prsf from MeteoData order by fecha desc limit 1;"
    return run(connection, statement)

def getAvg(connection):
    statement = "SELECT AVG(temp) as tempf,AVG(hum) as humf,AVG(luz) as ligf,AVG(pres) as prsf FROM MeteoData WHERE fecha>date_sub(now(),interval 1 day);"
    return run(connection, statement)

def getMax(connection):
    statement = "SELECT MAX(temp) as tempf,MAX(hum) as humf,MAX(luz) as ligf,MAX(pres) as prsf FROM MeteoData WHERE fecha>date_sub(now(),interval 1 day);"
    return run(connection, statement)

def getMin(connection):
    statement = "SELECT MIN(temp),MIN(hum),MIN(luz),MIN(pres) FROM MeteoData WHERE fecha>date_sub(now(),interval 1 day);"
    return run(connection, statement)

# See available languages and text ids in the setupDB.sql file
def getTranslation(connection, txt_id, lang_code):
    available_lang_codes = ['EN', 'ES']
    if lang_code in available_lang_codes:
        statement = 'SELECT {} FROM Lang WHERE ID = \'{}\''.format(lang_code, txt_id);
        resultado = run(connection, statement)
        primer = resultado.next()
        texto = primer[0]
        return texto
    else:
        sprint(lang_code, 'is not an available language code')
