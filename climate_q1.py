import matplotlib.pyplot as plt
import sqlite3

db_connection = sqlite3.connect('climate.db')
cursor = db_connection.cursor()

queries = [
    "SELECT Year FROM ClimateData",
    "SELECT CO2 FROM ClimateData",
    "SELECT Temperature FROM ClimateData"
]

cursor.execute(queries[0])
years = cursor.fetchall()
cursor.execute(queries[1])
co2 = cursor.fetchall()
cursor.execute(queries[2])
temp = cursor.fetchall()

cursor.close()
db_connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png")
