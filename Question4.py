
# # Question 4: SQL and Python
# Bike rental company

# # Code Section


import sqlite3

# It is important to maintain the database file in the same folder of this jupyter notebook
db = sqlite3.connect("bikecompany.db")
db.isolation_level = None

"""

This function retrieves the total distance that the specified user has driven. E.g.
print("Test 1:", distance_of_user("user123"))
and if implemented correctly it should output:
Test 1: 130160

"""

def distance_of_user(user):
    dist_of_user = db.execute(
        f"""SELECT SUM(distance)
        FROM Trips 
        INNER JOIN Users ON Trips.user_id = Users.id 
        WHERE Users.name=?;""", [user]).fetchone()
    return print(f'In total, the {user} has driven {dist_of_user[0]} meters')


"""
This function retrieves the average speed for all trips driven by a specific user rounding to two decimal spaces. E.g.
print("Test 2:", speed_of_user("user123"))
and if implemented correctly it should output:
Test 2: 17.35
"""


def speed_of_user(user):
    avg_spd_of_user = db.execute(
        f"""SELECT ROUND((all_distance / all_duration),2)
        FROM (SELECT Users.name,SUM(distance)/1000.00 all_distance,SUM(duration)/60.00 all_duration
        FROM Trips
        INNER JOIN Users ON Users.id = Trips.user_id
        WHERE Users.name=?);""", [user]).fetchone()
    return print(f'The average speed for all trips driven by {user} is {avg_spd_of_user[0]} km/h.')


"""

This function retrieves for each city how long all bikes in the city were driven in total during the given day. E.g.
print("Test 3:", duration_in_each_city("2021-06-01"))
and if implemented correctly it should output:
Test 3: [('city1', 58655), ('city10', 59296), ('city2', 60947)…]
"""


def duration_in_each_city(day):
    dur_in_city_per_day = db.execute(
        f"""SELECT C.name, SUM(T.duration)
        FROM Bikes B, Trips T, Cities C
        WHERE B.city_id = C.id AND B.id = T.bike_id AND T.day=?
        GROUP BY C.id LIMIT 10""", [day]).fetchall()
    listcities = dur_in_city_per_day
    for row in listcities:
        print(f"In the {row[0]},the bikes were driven: {row[1]} min.")


"""

This function retrieves for how many different users used the bikes in the given city. E.g
print("Test 4:", users_in_city("city5"))
and if implemented correctly it should output:
Test 4: 43102

"""


def users_in_city(city):
    users_city = db.execute(
        f"""SELECT COUNT(DISTINCT user_id), cities.name
        FROM Trips
        INNER JOIN Stops ON Trips.from_id = Stops.id
        INNER JOIN Cities ON Stops.city_id = Cities.id
        WHERE cities.name=?
        GROUP BY cities.name""", [city]).fetchone()
    return print(f'The trips made in the {city} are {users_city[0]}')


"""

This function retrieves how many trips were driven each day in the given city.
print("Test 5:", trips_on_each_day("city5"))
and if implemented correctly it should output:
Test 5: [('2021-06-01', 3362), ('2021-06-02', 3345),…]

"""

def trips_on_each_day(city):
    trips_in_aCity_each_day = db.execute(
        f"""SELECT day, COUNT(id)
         FROM Trips 
         WHERE from_id IN (SELECT Stops.id 
                           FROM Cities, Stops
                           WHERE Cities.id = Stops.city_id AND Cities.name=?)
                           GROUP BY day""", [city]).fetchall()

    return print(trips_in_aCity_each_day)

"""

This function retrieves the most popular starting location and the number of trips starting from that stop.
print("Test 6:", most_popular_start("city5"))
and if implemented correctly it should output:
Test 6: ('stop419', 1073)

"""


def most_popular_start(city):
    stop_popular = db.execute(
        f"""SELECT STOP, MAX(travelsmade), City
    FROM(SELECT Stops.name STOP, Cities.name City, COUNT(DISTINCT Trips.id) AS travelsmade
    FROM Trips
    INNER JOIN Stops ON Trips.from_id = Stops.id
    INNER JOIN Cities ON Stops.city_id = Cities.id
    GROUP BY Stops.name)
    WHERE City=?""", [city]).fetchone()
    return print(f'The most popular stop of the {city} is: {stop_popular[0]} with {stop_popular[1]} stops')


# # Testing Section



if __name__ == "__main__":
    test_user = "user123"
    test_city = 'city5'
    test_day = "2021-06-01"


# Function 1



distance_of_user(test_user)


# Function 2



speed_of_user(test_user)


# Function 3



duration_in_each_city(test_day)


# Function 4



users_in_city(test_city)


# Function 5



trips_on_each_day(test_city)


# Function 6



most_popular_start(test_city)


# # Try another day, cities or users

# Function 1



print('\nDISTANCE TRAVELLED BY USER')
name1 = input('Enter the name of the user:')
distance_of_user(name1)


# Function 2



print('\nAVERAGE SPEED OF THE USER')
name2 = input('Enter the name of the user:')
speed_of_user(name2)


# Function 3


print('\nDURATION IN EACH CITY')
day1 = input('Enter the day:')
duration_in_each_city(day1)


# Function 4


print('\nUSERS IN A CITY')
city1 = input('Enter the name of the city:')
users_in_city(city1)


# Function 5


print('\nTRIPS ON EACH DAY ')
city2 = input('Enter the name of the city:')
trips_on_each_day(city2)


# Function 6



print('\nMOST POPULAR LOCATION ')
city3 = input('Enter the name of the city:')
most_popular_start(city3)