# Andy Luong 1525166
# CIS 3368 Exam 1

# import requests & json to get information from websites. Imported hello to get the database connections.
# import sys to stop during try except blocks if it catches an error.
import requests 
import json
import hello
import sys

# creating a variable to create a connection
connection = hello.create_connection("cis3368.cjnu6pcvcl5h.us-east-1.rds.amazonaws.com", "andyluong", "Greenyellowrhino123!", "cis3368db")

# inputting the state and date in order to get covid data 
# added try except block with AssertionError to catch if the input is in letters. If it is not in letters, it will catch exception.
try:
    state = input("Enter the state for which the COVID data should be retrieved (e.g. TX): ")
    # assert keyword tests if user entered a letter. If it is false, it raises an error.
    assert state.isalpha()
except AssertionError:
    print("You entered a number. Please enter two capital letters with no spaces afterwards.")
    # sys.exit(1) will stop the program because an error was found.
    sys.exit(1)

# added try except block with ValueError to see if the input is an integer or not. If it is not a number, then it will catch exception.
try:
    date = int(input("Enter the date for which the COVID data should be retrieved (e.g. 20201219): "))
except ValueError:
    print("You entered a letter. Please enter numbers in year, month, and days format.")
    # sys.exit(1) will stop the program because an error was found.
    sys.exit(1)

# create exam1 table
create_exam1_table = """
CREATE TABLE IF NOT EXISTS exam1(
id INT AUTO_INCREMENT,
date DateTime,
state VARCHAR(2) NOT NULL,
positiveIncrease INT NOT NULL,
deathIncrease INT NOT NULL,
PRIMARY KEY (id)
)"""

# executes statement above, creating the table 
hello.execute_query(connection, create_exam1_table)

# getting website data by using requests.get method. Formatting the link with state and date that user inputs. 
response = requests.get("https://api.covidtracking.com/v1/states/{}/{}.json".format(state, date))
# converting the website data into json format
json_response = response.json()

# parsing through json data by specifying keys, which gives us the values associated with it.
positive_cases = json_response["positiveIncrease"]
deaths = json_response["deathIncrease"]

# adding the information into database by formatting user inputs and parsed json data, then executing the SQL statement.
query = "INSERT INTO exam1 (date, state, positiveIncrease, deathIncrease) VALUES (%s, '%s', %s, %s)" % (date, state, positive_cases, deaths)
hello.execute_query(connection, query)
print()

# printing covid data based on state & date which was inputted, as well as positive cases & deaths by parsing json data.
print("state:", state)
print("date:", date)
print("positive cases:", positive_cases)
print("death:", deaths)