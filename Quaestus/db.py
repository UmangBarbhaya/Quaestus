import csv, sqlite3

con = sqlite3.connect("database.db")
print("Opened database successfully");
cur = con.cursor()
cur.execute("CREATE TABLE PRODUCT (Product_ID TEXT, Product_Name TEXT,Domain TEXT,Product_Price TEXT);") # use your column names here
print("Tables created successfully");
with open('Baby_Product_Table.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i["Product_ID"], i["Product_Name"],i["Domain"],i["Product_Price"]) for i in dr]

cur.executemany("INSERT INTO PRODUCT (Product_ID, Product_Name,Domain,Product_Price) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
print("done")
