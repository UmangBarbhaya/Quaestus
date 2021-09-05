from flask import Flask, render_template,session, redirect, url_for, escape, request
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = "itssecret"

@app.route('/')
def Quaestus():
   if 'username' in session:
      return redirect(url_for('Quaestus'))
   return render_template("Quaestus.html")
   

@app.route('/ProductList')
def ProductList():
   if 'username' in session:
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      
      cur = con.cursor()
      cur.execute("select * from PRODUCT")
      
      rows = cur.fetchall();
      return render_template("ProductList.html",rows = rows)
   return redirect(url_for('Quaestus'))


@app.route('/ProductDisplay/<para>')
def ProductDisplay(para):
   if 'username' in session:
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      
      cur = con.cursor()
      cur.execute("select * from PRODUCT where Product_ID=?",[para])
      
      rows = cur.fetchall();
      return render_template("ProductDisplay.html",rows = rows)
   return redirect(url_for('Quaestus'))


@app.route('/Clogin', methods = ['GET', 'POST'])
def Clogin():
   if request.method == 'POST':
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      cur = con.cursor()

      cur.execute("select Cust_ID from CUST where Cust_Username=? AND Cust_PWord=?",[request.form['username'],request.form['password']])
      rows = cur.fetchall();
         
      if len(rows)>0:
         session['username'] = request.form['username']
         return redirect(url_for('ProductList'))
      return redirect(url_for('Quaestus'))
      
      

@app.route('/Slogin', methods = ['GET', 'POST'])
def Slogin():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('SellerProductList'))


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   #session.pop('username', None)
   session.clear()
   return redirect(url_for('Quaestus'))

if __name__ == '__main__':
   app.run(debug = True)
   
