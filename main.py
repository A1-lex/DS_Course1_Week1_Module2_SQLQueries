`import os
import sqlite3

import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _connect(database_name: str) -> sqlite3.Connection:
    return sqlite3.connect(os.path.join(BASE_DIR, database_name))


conn1 = _connect("planets.db")
df_no_moons = pd.read_sql(
    "SELECT * FROM planets WHERE num_of_moons = 0;",
    conn1,
)
df_name_seven = pd.read_sql(
    "SELECT name, mass FROM planets WHERE LENGTH(name) = 7;",
    conn1,
)
df_mass = pd.read_sql(
    "SELECT name, mass FROM planets WHERE mass <= 1.00;",
    conn1,
)
df_mass_moon = pd.read_sql(
    "SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00;",
    conn1,
)
df_blue = pd.read_sql(
    "SELECT name, color FROM planets WHERE color LIKE '%blue%';",
    conn1,
)


conn2 = _connect("dogs.db")
df_hungry = pd.read_sql(
    "SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;",
    conn2,
)
df_hungry_ages = pd.read_sql(
    "SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC;",
    conn2,
)
df_4_oldest = pd.read_sql(
    "SELECT name, age, breed FROM (SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4) ORDER BY breed ASC;",
    conn2,
)


conn3 = _connect("babe_ruth.db")
df_ruth_years = pd.read_sql(
    "SELECT COUNT(year) AS total_years FROM babe_ruth_stats;",
    conn3,
)
df_hr_total = pd.read_sql(
    "SELECT SUM(HR) AS total_HR FROM babe_ruth_stats;",
    conn3,
)
df_ruth_years = pd.read_sql(
    "SELECT team, COUNT(year) AS number_years FROM babe_ruth_stats GROUP BY team;",
    conn3,
)
df_at_bats = pd.read_sql(
    "SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200;",
    conn3,
)
