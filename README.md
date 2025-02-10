# job_portal
# Job Application Tracker

## 📌 Project Overview
The **Job Application Tracker** is a Flask-based web application that helps users track job applications, store details, and monitor progress. It provides features like adding job entries, updating statuses, and filtering applications based on different criteria.

## 🚀 Features
- User Authentication (Login & Register)
- Add, Edit, and Delete Job Applications
- View All Applied Jobs
- Search and Filter Jobs by Status
- Store Additional Details like Resume Uploads
- Flask-Migrate for Database Management

## 🏗️ Project Structure
```
/job_tracker
│── /templates            # HTML Templates
│    │── index.html       # Home Page - List Jobs
│    │── login.html       # Login Page
│    │── register.html    # Registration Page
│── /static               # CSS, JS, Images
│── /migrations           # Flask-Migrate files
│── app.py                # Main Flask App
│── models.py             # Database Models
│── forms.py              # WTForms for Forms
│── config.py             # App Configuration
│── requirements.txt      # Dependencies
│── database.db           # SQLite Database (Auto-generated)
│── .gitignore            # Ignore unnecessary files
│── README.md             # Project Documentation
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/job_tracker.git
cd job_tracker
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5️⃣ Run the Application
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000/`.

## 🔑 Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
DEBUG=True
```

## 📌 Usage Guide
1. **Register/Login** to access the application.
2. **Add New Jobs** by providing company name, position, and date applied.
3. **View, Edit, or Delete** job applications as needed.
4. **Track Your Applications** with different statuses like "Applied", "Interview Scheduled", etc.

## 🛠️ Technologies Used
- **Flask** (Backend Framework)
- **Flask-SQLAlchemy** (Database ORM)
- **Flask-Migrate** (Database Migrations)
- **WTForms** (Form Handling)
- **SQLite** (Database)
- **HTML, CSS** (Frontend UI)

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-new`).
3. Commit your changes and push to GitHub.
4. Create a pull request!
