# Andy Luong 1525166
# CIS 3368 Homework 1

import datetime
from datetime import date
import time
import mysql.connector
from mysql.connector import Error

class Contact:
  def __init__(self, id, contactDetails, creationDate):
    self.id = id
    self.contactDetails = contactDetails
    self.creationDate = creationDate

def create_connection(host_name, user_name, user_password, db_name): # create connection to database
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query): # executes an sql statement
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query): # reads the database
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



connection = create_connection("cis3368.cjnu6pcvcl5h.us-east-1.rds.amazonaws.com", "andyluong", "Greenyellowrhino123!", "cis3368db")

# creating our table 
create_contacts_table = """
CREATE TABLE IF NOT EXISTS contacts(
id INT AUTO_INCREMENT,
contactDetails VARCHAR(255) NOT NULL,
creationDate date,
PRIMARY KEY (id)
)"""

# executes statement above, creating the table 
execute_query(connection, create_contacts_table)

# add contact to contacts table
def add_Contact():
    # gets today's date in string format
    now = time.strftime("%Y-%m-%d") 
    contact_details = input("Enter contact details: ")
    # creating sql statement that inserts information inside database
    query = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s', '%s')" % (contact_details, now)
    # executes insert sql statement
    execute_query(connection, query)

# updating contact in contacts table
def update_Contact():
    contact_id = int(input("Enter an id number: "))
    new_contact_details = input("Enter new contact details: ")
    # creating sql statement that updates information inside database
    # it updates contactDetails depending on the id that user entered
    update_contact_query = """ 
    UPDATE contacts
    SET contactDetails = '%s'
    WHERE id = %s """ % (new_contact_details, contact_id)
    # executes update sql statement
    execute_query(connection, update_contact_query)

# delete contact record from contact table
def remove_Contact():
    contact_id_to_delete = int(input("Enter id to delete: "))
    # sql statement that deletes a contact depending on id user entered
    delete_statement = "DELETE FROM contacts WHERE id = %s" % (contact_id_to_delete)
    # executes delete sql statement
    execute_query(connection, delete_statement)

# output all contacts in alphabetical order
def output_contacts_alphabetically():
    # selects all contacts alphabetically from A to Z 
    select_contacts_alphabetically = "SELECT * FROM contacts ORDER BY contactDetails"
    # creating a variable that holds the sorted database
    contacts_alphabet = execute_read_query(connection, select_contacts_alphabetically)
    # for each row in sorted database, prints each row
    for (id, contactDetails, creationDate) in contacts_alphabet:
        print(id, contactDetails, creationDate)
    print()

# output all contacts by creation date
def output_contacts_date():
    # selects all contacts by creation date from smallest to largest
    select_contacts_date = "SELECT * FROM contacts ORDER BY creationDate"
    # creating a variable that holds the sorted database
    contacts_date = execute_read_query(connection, select_contacts_date)
    # for each row in sorted database, prints each row
    for (id, contactDetails, creationDate) in contacts_date:
        print(id, contactDetails, creationDate)
    print()

# output all contacts    
def output_contacts():
    # selects entire table 
    select_contacts = "SELECT * FROM contacts"
    # created variable that holds entire database
    contacts = execute_read_query(connection, select_contacts)
    # for each row in database, prints each row
    for (id, contactDetails, creationDate) in contacts:
        print(id, contactDetails, creationDate)
    print()
        
# menu that allows that shows you options
menu = ("MENU\n"
"a - Add contact\n"
"d - Remove contact\n"
"u - Update contact details\n"
"b - Output all contacts in alphabetical order\n"
"c - Output all contacts by creation date\n"
"o - Output all contacts\n"
"q - Quit\n")

# created while loop that displays the menu and allows you to choose an option. If it its not a valid input, it will keep outputting menu.
# once a valid input is accepted, it will execute the function.
command = ''
while command != "q":
    print(menu)
    command = input("Choose an option: ")
    while command != "a" and command != "d" and command != "u" and command != "b" and command != "c" and command != "o" and command != "q":
        command = input("Choose an option: ")
    if command == "a":
        add_Contact()
    elif command == "d":
        remove_Contact()
    elif command == "u":
        update_Contact()
    elif command == "b":
        output_contacts_alphabetically()
    elif command == "c":
        output_contacts_date()
    elif command == "o":
        output_contacts()