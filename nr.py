import sys
import json
import MySQLdb
from MySQLdb import escape_string as thwart

reload(sys)
sys.setdefaultencoding('ISO-8859-1')

mysql = MySQLdb
connection = mysql.connect(host = "localhost", user = "root", passwd = "HiGroup6!", db = "Easycook")
cursor = connection.cursor()


fname = 'klikk-recipes-backup.json'
str_data = open(fname).read()
json_data = json.loads(str_data)
i = 0

for entry in json_data:
	i += 1
	print("i", i)
	title = entry['title']
	#print(title)
	ingredients = entry['ingredients']
	
	cursor.execute('''SELECT name_R From Recipe Where name_R='%s';'''%(thwart(title)))
	check = cursor.fetchall()
	if check!=():
		continue
	#print(type(ingredients))
	#for j in ingredients:
		#print(j)
		#print('''INSERT INTO Ingredient(name_I, name_R) VALUES('%s', '%s');'''%(MySQLdb.escape_string(j),MySQLdb.escape_string(title)))
		#cursor.execute('''INSERT INTO Ingredient(name_I, name_R) VALUES('%s', '%s');'''%(MySQLdb.escape_string(j), MySQLdb.escape_string(title)))
		#connection.commit()
	#print(ingredients)
	st ="['"+ "', '".join(ingredients)+"']"
	print(st)
	#print('''INSERT INTO aaa (name_R,ingredients,categories,rating) VALUES('%s', '%s', '%s',0);'''%(title, st, st))
	cursor.execute('''INSERT INTO Recipe (name_R,ingredients,categories,rating) VALUES('%s', '%s', '%s',0);'''%(thwart(title), thwart(st), thwart(st)))
	connection.commit()
	#if i==1000:
	#	break

cursor.close()
connection.close()


