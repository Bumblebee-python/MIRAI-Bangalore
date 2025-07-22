# MIRAI-Bangalore

Here is a well-structured `README.md` file for your **Library Management System** project that you can use on GitHub. It includes:

* Project summary
* Features mapped to the original question
* Tech stack
* Screenshots placeholders
* Setup instructions
* SQL design for relationships and constraints
* How each feature works

---

### 📄 `README.md`

````markdown
# 📚 Library Management System

A simple Flask-based backend web application for managing **Books**, **Borrowers**, and **Book Issues**. This project demonstrates database operations, constraint enforcement, and many-to-many relationships using a MySQL database.

---

## ✅ Project Requirements (Fully Met)

| Requirement | Implemented |
|-------------|-------------|
| 1. CRUD for Books, Authors, and Borrowers | ✅ via MySQL and auto-reflect in UI |
| 2. Borrow a Book | ✅ `Loan` entry is created if not already issued |
| 3. Return a Book | ✅ Updates `return_date` |
| 4. Track Overdue Books | ✅ `/overdue` route displays them |
| Test on Many-to-Many (Books ↔ Authors) | ✅ `book_author` table |
| Unique Book Issue Constraint | ✅ via query check |
| Query Logic for Overdue Loans | ✅ via SQL + Flask |

---

## 🔧 Tech Stack

- **Python 3.8+**
- **Flask**
- **MySQL**
- **HTML + Bootstrap**
- **MySQL Connector for Python**

---

## 🖼️ Screenshots

> You can capture and upload these screenshots and link them here.

### 🏠 Home Page (`/`)
Displays all books with actions to **Borrow** and **Return**.

![Home Page](screenshots/home.png)

---

### ⏰ Overdue Books (`/overdue`)
Shows books borrowed more than 7 days ago.

![Overdue Page](screenshots/overdue.png)

---

## 🧠 Database Design

### Books Table
```sql
CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100)
);
````

### Authors Table

```sql
CREATE TABLE authors (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);
```

### Borrowers Table

```sql
CREATE TABLE borrowers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);
```

### Loans Table

```sql
CREATE TABLE loans (
  id INT AUTO_INCREMENT PRIMARY KEY,
  book_id INT,
  borrower_id INT,
  issue_date DATETIME,
  return_date DATETIME
);
```

### Book ↔ Author (Many-to-Many)

```sql
CREATE TABLE book_author (
  book_id INT,
  author_id INT,
  PRIMARY KEY (book_id, author_id)
);
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database

Create schema and insert sample data:

```sql
-- In MySQL client:
SOURCE setup.sql; -- (provided SQL file with sample books, authors, borrowers, loans)
```

> 📌 Don't forget to update your MySQL username/password in `app.py`.

---

## ▶️ Run the Application

```bash
python app.py
```

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Key Features Demonstrated

### ✅ CRUD Operations

* Books, Authors, and Borrowers can be added/edited/deleted via MySQL.
* Reflected in UI automatically.

### ✅ Borrowing Logic

* Book can be borrowed only if it’s not already issued.
* Stored in `loans` table with `NULL` return\_date.

### ✅ Return Logic

* Updates `return_date` in `loans` table.

### ✅ Overdue Tracking

* `/overdue` route shows books not returned and issued >7 days ago.

---

## 🧠 Advanced Concepts

* **Many-to-Many Relation**: `book_author` table handles books with multiple authors.
* **Unique Constraint Logic**: Prevents borrowing the same book if it's already issued.
* **Overdue Query Logic**:

```sql
SELECT b.title, l.issue_date 
FROM loans l
JOIN books b ON l.book_id = b.id
WHERE l.return_date IS NULL
AND l.issue_date < NOW() - INTERVAL 7 DAY;
```

---

## ✍️ Author

**Bijesh Thomas**
📍 CHRIST (Deemed to be University), Pune Lavasa Campus
📫 [LinkedIn](https://linkedin.com/in/your-profile) (optional)

---

## 📜 License

This project is open-source and free to use for educational purposes.

```

---

### 📝 Notes:
- Replace screenshot paths (`screenshots/home.png`) after uploading images.
- Add your actual GitHub repo link and update `git clone` line.
- You can save your SQL in `setup.sql` and mention it in the readme.

Would you like me to also generate the `setup.sql` file with all sample data?
```
