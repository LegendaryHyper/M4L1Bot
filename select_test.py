import sqlite3

con = sqlite3.connect("movie.db")

cur = con.cursor()

#cur.execute("SELECT title FROM movies")
#cur.execute("SELECT popularity FROM movies") # inner join gerekebilir

cur.execute("SELECT vote_average, title FROM movies ORDER BY vote_average LIMIT 8 OFFSET 50")

result = cur.fetchall()

con.close()

for row in result:
    print(row)