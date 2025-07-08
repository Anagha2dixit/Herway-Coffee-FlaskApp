from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# 🔌 Connect to database
def get_db_connection():
    db_path = 'database/herway.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# 🧱 Initialize DB from schema.sql if not exists
def initialize_db():
    if not os.path.exists('database/herway.db'):
        conn = get_db_connection()
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

# 🏠 Home route
@app.route('/')
def home():
    return redirect('/customers')

# 📄 List customers
@app.route('/customers')
def customers():
    conn = get_db_connection()
    customers = conn.execute("SELECT * FROM customers").fetchall()
    conn.close()
    return render_template('customers.html', customers=customers)

# ➕ Add customer
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

# ✏️ Edit form
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

# 🚀 Start Flask app on public IP for Render
if __name__ == "__main__":
    initialize_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


