from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 🔌 Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database/herway.db')
    conn.row_factory = sqlite3.Row
    return conn

# 🏠 Home route (redirects to customer list)
@app.route('/')
def home():
    return redirect('/customers')

# 📄 Display all customers
@app.route('/customers')
def customers():
    conn = get_db_connection()
    customers = conn.execute("SELECT * FROM customers").fetchall()
    conn.close()
    return render_template('customers.html', customers=customers)

# ➕ Add new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO customers (name, email, phone, address)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, address))
    conn.commit()
    conn.close()
    return redirect('/customers')

# ✏️ Show edit form
@app.route("/edit_customer/<int:customer_id>")
def edit_customer(customer_id):
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,)).fetchone()
    conn.close()
    return render_template("edit_customer.html", customer=customer)

# 💾 Update customer
@app.route("/update_customer/<int:customer_id>", methods=["POST"])
def update_customer(customer_id):
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]

    conn = get_db_connection()
    conn.execute("""
        UPDATE customers
        SET name = ?, email = ?, phone = ?, address = ?
        WHERE customer_id = ?
    """, (name, email, phone, address, customer_id))
    conn.commit()
    conn.close()
    return redirect("/customers")

# ❌ Delete customer
@app.route("/delete_customer/<int:customer_id>", methods=["POST"])
def delete_customer(customer_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
    conn.commit()
    conn.close()
    return redirect("/customers")

# 🏁 Start the app
if __name__ == '__main__':
    app.run(debug=True)
