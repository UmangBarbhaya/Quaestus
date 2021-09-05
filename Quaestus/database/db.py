import csv, sqlite3

con = sqlite3.connect("database.db")
print("Opened database successfully");
cur = con.cursor()


cur.execute("CREATE TABLE SELLER (Seller_ID TEXT Primary key, Seller_Name TEXT,Seller_Address TEXT,Seller_Phone TEXT,Seller_Email TEXT);")
cur.execute("CREATE TABLE PRODUCT (Product_ID TEXT Primary key, Product_Name TEXT,Domain TEXT,Product_Price TEXT);")

cur.execute("CREATE TABLE SELLER_PRODUCT (Seller_SP_ID TEXT, Product_SP_ID TEXT, Stock_Left TEXT, Product_Discount TEXT, primary key(Seller_SP_ID,Product_SP_ID),foreign key(Seller_SP_ID) references SELLER(Seller_ID) ON DELETE CASCADE ON UPDATE NO ACTION, foreign key(Product_SP_ID) references PRODUCT(Product_ID) ON DELETE CASCADE ON UPDATE NO ACTION);")

cur.execute("CREATE TABLE CUST(Cust_ID TEXT Primary Key, Cust_Name TEXT, Cust_Username Text, Cust_Pword Text, Age Text, Cust_Phone Text, Cust_Email Text);")

cur.execute("CREATE TABLE PURCHASE(Cust_P_ID TEXT, SELLER_P_ID TEXT, Product_P_ID TEXT, Number_Items Text, Date_Of_Purchase Text, Unix_Time_Purchase TEXT, Purchase_Price TEXT, Mode_Of_Payment Text, Item_Status TEXT, Review TEXT, Summary TEXT, Rating TEXT, Helpfulness TEXT, Primary key(Cust_P_ID, SELLER_P_ID, Product_P_ID),foreign key(Product_P_ID) references PRODUCT(Product_ID) ON DELETE CASCADE ON UPDATE NO ACTION,foreign key(Cust_P_ID) references CUST(Cust_ID) ON DELETE CASCADE ON UPDATE NO ACTION,foreign key(Seller_P_ID) references SELLER(Seller_ID) ON DELETE CASCADE ON UPDATE NO ACTION);")

cur.execute("CREATE TABLE ORDER_DETAILS(Order_ID TEXT, Seller_OD_ID TEXT, Product_OD_ID TEXT, Ouantity TEXT, Intended_Delivery_ Date TEXT, Mode_of_Payment TEXT, Primary key(Order_ID, Seller_OD_ID, Product_OD_ID), foreign key(Seller_OD_ID) references SELLER(Seller_ID) ON DELETE CASCADE ON UPDATE NO ACTION,foreign key(Product_OD_ID) references PRODUCT(Product_ID) ON DELETE CASCADE ON UPDATE NO ACTION);")


print("Tables created successfully");

#inserting values into product table
with open('Product_Table.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i["Product_ID"], i["Product_Name"],i["Domain"],i["Product_Price"]) for i in dr]

cur.executemany("INSERT INTO PRODUCT (Product_ID, Product_Name,Domain,Product_Price) VALUES (?, ?, ?, ?);", to_db)

#inserting value into seller table
with open('Seller_Table.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i["Seller_ID"], i["Seller_Name"],i["Seller_Address"],i["Seller_Phone"],i["Seller_Email"]) for i in dr]

cur.executemany("INSERT INTO SELLER (Seller_ID, Seller_Name,Seller_Address,Seller_Phone,Seller_Email) VALUES (?, ?, ?, ?, ?);", to_db)

#inserting value into seller product table
with open('Seller_Product_Table.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i["Seller_SP_ID"], i["Product_SP_ID"],i["Stock_Left"],i["Product_Discount"]) for i in dr]

cur.executemany("INSERT INTO SELLER_PRODUCT (Seller_SP_ID, Product_SP_ID,Stock_Left,Product_Discount) VALUES (?, ?, ?, ?);", to_db)

with open('Customer_Table.csv','rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i["Customer_ID"], i["Customer_Name"],i["Customer_Username"],i["Customer_Pword"],i["Customer_Age"],i["Customer_Phone"],i["Customer_Email"]) for i in dr]

cur.executemany("INSERT INTO CUST (Cust_ID, Cust_Name,Cust_Username,Cust_Pword,Age,Cust_Phone,Cust_Email) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)


con.commit()
con.close()
print("done")
