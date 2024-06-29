import sqlite3

def connect():
    try:
        connectionObject = sqlite3.connect("person_db.db")
        print('connected to database successfully')
        return connectionObject
    except:
        print('Database connectivity failed')

def createDatabase():
    sqlQuery = "CREATE DATABASE IF NOT EXISTS person_db;"
    connecttionObject = connect()
    connecttionObject.execute(sqlQuery)
    connecttionObject.close()

def createTable():
    sqlQuery = """CREATE TABLE IF NOT EXISTS persons(id integer primary key autoincrement, name varchar(32) not null, gender varchar(2));"""
    try:
        connectionObject = connect()
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sqlQuery)
        cursorObject.close()
        connectionObject.close()
    except:
        print('Table creation failed')

class Person:
    def __init__(self, id=None, name='', gender=None):
        self.name = name 
        if id != None:
            self.id = id
        if gender != None:
            self.gender = gender

def listAllPersons():    
    sqlQuery = """SELECT * FROM persons"""
    parameters = tuple()
    connectionObject = connect()
    cur = connectionObject.cursor()
    response = cur.execute(sqlQuery, parameters)
    persons = []
    result_persons = response.fetchall()
    for e in result_persons:
        persons.append(Person(id=e[0], name=e[1], gender=e[2]))
    cur.close()
    connectionObject.close()
    return persons 

'''
def insertNewPerson():
    sqlQuery = """insert into persons(name, gender) values(?, ?)"""
    name, gender = input('Enter name and gender of the person: ').split()
    person = (name, gender)
    connectionObject = connect()
    cur = connectionObject.cursor()
    cur.execute(sqlQuery, person)
    cur.close()
    connectionObject.close()
'''

persons = listAllPersons()
print('%-3s %-14s %-2s'%('ID', 'NAME', 'GENDER'))
for person in persons:
    print('%-3s %-15s %-2s'%(person.id, person.name, person.gender))