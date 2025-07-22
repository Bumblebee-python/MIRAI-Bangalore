from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)

# DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="library_db"
)
cursor = conn.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template("index.html", books=books)

@app.route('/borrow/<int:book_id>')
def borrow(book_id):
    cursor.execute("SELECT * FROM loans WHERE book_id=%s AND return_date IS NULL", (book_id,))
    loan = cursor.fetchone()
    if loan:
        return "Book already issued!"
    cursor.execute("INSERT INTO loans (book_id, borrower_id, issue_date) VALUES (%s, %s, %s)",
                   (book_id, 1, datetime.now()))
    conn.commit()
    return redirect('/')

@app.route('/return/<int:book_id>')
def return_book(book_id):
    cursor.execute("UPDATE loans SET return_date=%s WHERE book_id=%s AND return_date IS NULL",
                   (datetime.now(), book_id))
    conn.commit()
    return redirect('/')

@app.route('/overdue')
def overdue():
    cursor.execute("""
        SELECT b.title, l.issue_date 
        FROM loans l JOIN books b ON l.book_id = b.id 
        WHERE l.return_date IS NULL AND l.issue_date < %s
    """, (datetime.now() - timedelta(days=7),))
    overdue_books = cursor.fetchall()
    return render_template("index.html", books=overdue_books)

if __name__ == '__main__':
    app.run(debug=True)
