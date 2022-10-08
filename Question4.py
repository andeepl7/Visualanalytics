import sqlite3
import pandas as pd

db = sqlite3.connect("bikecompany.db")
db.isolation_level = None


"""

This function retrieves the total distance that the specified user has driven. E.g.
print("Test 1:", distance_of_user("user123"))
and if implemented correctly it should output:
Test 1: 130160

"""
def total_distance(user):
    df = pd.read_sql_query(
        r"""SELECT name,SUM(distance) AS Totaldistance 
        FROM Trips 
        INNER JOIN Users ON Trips.user_id = Users.id 
        GROUP BY user_id""", db)
    df = df.set_index('name')
    return print(f'The total distance of the {user} is: {df.at[user, "Totaldistance"]}')


"""
This function retrieves the average speed for all trips driven by a specific user rounding to two decimal spaces. E.g.
print("Test 2:", speed_of_user("user123"))
and if implemented correctly it should output:
Test 2: 17.35
"""

def speed_of_user(user):
    df1 = pd.read_sql_query(
        r"""SELECT User, all_distance / all_duration AS Speed
        FROM (SELECT Users.name User,SUM(distance)/1000.00 all_distance ,SUM(duration)/60.00 all_duration
        FROM Trips
        INNER JOIN Users
        ON Users.id = Trips.user_id
        GROUP BY Users.name)""", db)
    df1 = df1.set_index('User')
    return print(f'The speed of the {user} is: {df1.at[user, "Speed"]}')

"""

This function retrieves for each city how long all bikes in the city were driven in total during the given day. E.g.
print("Test 3:", duration_in_each_city("2021-06-01"))
and if implemented correctly it should output:
Test 3: [('city1', 58655), ('city10', 59296), ('city2', 60947)…]
"""


def duration_in_each_city(day):
    pass


"""

This function retrieves for how many different users used the bikes in the given city. E.g
print("Test 4:", users_in_city("city5"))
and if implemented correctly it should output:
Test 4: 43102

"""


def users_in_city(city):
    pass


"""

This function retrieves how many trips were driven each day in the given city.
print("Test 5:", trips_on_each_day("city5"))
and if implemented correctly it should output:
Test 5: [('2021-06-01', 3362), ('2021-06-02', 3345),…]

"""


def trips_on_each_day(city):
    pass


"""

This function retrieves the most popular starting location and the number of trips starting from that stop.
print("Test 6:", most_popular_start("city5"))
and if implemented correctly it should output:
Test 6: ('stop419', 1073)

"""


def most_popular_start(city):
    pass

# Testing section

if __name__ == "__main__":
    test_user = "user123"
    total_distance(test_user)
    speed_of_user(test_user)