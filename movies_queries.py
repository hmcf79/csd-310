import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "port": "3006",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],
                                                                                      config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue...")
    cursor = db.cursor()
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: ", studio[0], )
        print("Studio Name: ", studio[1], "\n")

    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print ("Genre ID: ", genre[0], )
        print("Genre Name: ", genre[1], "\n")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime<120")
    shortFilms = cursor.fetchall()
    print ("-- DISPLAYING Short Film RECORDS --")
    for shortFilm in shortFilms:
        print ("Film Name: ", shortFilm[0], )
        print("Runtime: ", shortFilm[1], "\n")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    print ("-- DISPLAYING Director RECORDS In Order --")
    for director in directors:
        print ("Film Name: ", directors[0], )
        print ("Director: ", directors[1], "\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
    else:
        print(err)

finally:
    db.close()