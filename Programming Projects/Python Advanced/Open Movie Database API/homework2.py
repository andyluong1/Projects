# Andy Luong 1525166
# CIS 3368 Homework 2

# import requests & json to get information from websites. Imported hello to get the database connections.
import requests
import json
import hello

# creating a variable to create a connection
connection = hello.create_connection("cis3368.cjnu6pcvcl5h.us-east-1.rds.amazonaws.com", "andyluong", "Greenyellowrhino123!", "cis3368db")

# create results table. float datatype is for decimals; precision of 3 & scale of 1.
create_results_table = """
CREATE TABLE IF NOT EXISTS results(
id INT AUTO_INCREMENT,
title VARCHAR(100) NOT NULL,
year INT NOT NULL,
genre VARCHAR(100) NOT NULL,
rating FLOAT(3,1) NOT NULL,
PRIMARY KEY (id)
)"""

# executes statement above, creating the table 
hello.execute_query(connection, create_results_table)

def add_movie():
    # getting input for title and replacing white space with a "+" sign in order for the website to recognize it. 
    title = input("Enter movie title: ")
    title = title.replace(" ", "+")
    # getting website data by using requests.get method. Formatting the link with title that user inputs. 
    response = requests.get("http://www.omdbapi.com/?t={}&apikey=e4f420b3".format(title))
    # converting the website data into json format
    json_response = response.json()
    # parsing through json data by specifying keys, which gives us the values associated with it.
    movie_title = json_response["Title"]
    movie_year = json_response["Year"]
    movie_genre = json_response["Genre"]
    movie_rating = json_response["imdbRating"]
    # inserts information inside database; all of %s are strings because json data is in string format
    query = "INSERT INTO results (title, year, genre, rating) VALUES ('%s', '%s', '%s', '%s')" % (movie_title, movie_year, movie_genre, movie_rating)
    # executes insert sql statement
    hello.execute_query(connection, query)

def output_movies():
    # selects entire table
    select_movies = "SELECT * FROM results"
    # created variable that holds entire database and reads table 
    movies = hello.execute_read_query(connection, select_movies)
    # prints each row in database
    for x in movies:
        print(x)
    print()

def output_movies_ratings():
    # selects table by imdbRating from largest to smallest
    select_movies_rating = "SELECT * FROM results ORDER BY rating DESC"
    # created variable that holds entire database and reads table 
    movies_rating = hello.execute_read_query(connection, select_movies_rating)
    # prints each row in database
    for x in movies_rating:
        print(x)
    print()

def delete_rows():
    # input ID values from database to delete
    movie_id_x = int(input("Enter beginning ID value: "))
    movie_id_y = int(input("Enter ending ID value: "))
    # delete rows based on begin and end values. Using BETWEEN operator to delete everything between these 2 values.
    select_deleted_movies = "DELETE FROM results WHERE id BETWEEN %s AND %s" % (movie_id_x, movie_id_y)
    # execute delete sql statement
    hello.execute_query(connection, select_deleted_movies)
    
# menu that allows that shows you options
menu = ("MENU\n"
"a - Add movie\n"
"d - Remove rows\n"
"o - Output all movies\n"
"r - Output all movies by rating\n"
"q - Quit\n")

# created while loop that displays the menu and allows you to choose an option. If it its not a valid input, it will keep outputting menu.
# once a valid input is accepted, it will execute the function.
command = ''
while command != "q":
    print(menu)
    command = input("Choose an option: ")
    while command != "a" and command != "d" and command != "o" and command != "r" and command != "q":
        command = input("Choose an option: ")
    if command == "a":
        add_movie()
    elif command == "d":
        delete_rows()
    elif command == "o":
        output_movies()
    elif command == "r":
        output_movies_ratings()

# The menu option that does a meaningful operation is the output_movies_rating option. This allows you to see which movies by their rating score.
# I have completed the extra credit by implementing a delete functionality. The user selects a range of rows based on id that they want to be deleted.
# Be mindful that you have to output the movies to see the id number. Also, the ID is auto-incremented so the numbers are not in order one by one.