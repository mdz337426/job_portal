from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Job
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from models import db, User
from forms import LoginForm, RegisterForm, JobForm



app = Flask(__name__)
app.config.from_object("config.Config")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Home Route - Display Job Applications
@app.route("/")
def index():
    search_query = request.args.get('search', '')
    jobs = Job.query.order_by(Job.date_applied.desc()).all()
    return render_template("index.html", jobs=jobs, search_query=search_query)


# Add Job Route
@app.route("/add", methods=["GET", "POST"])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        new_job = Job(
            company=form.company.data,
            position=form.position.data,
            date_applied=form.date_applied.data,
            status=form.status.data
        )
        db.session.add(new_job)
        db.session.commit()
        flash("Job added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add_job.html", form=form)

# Edit Job Route
@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    form = JobForm(obj=job)
    if form.validate_on_submit():
        job.company = form.company.data
        job.position = form.position.data
        job.date_applied = form.date_applied.data
        job.status = form.status.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_job.html", form=form, job=job)

# Delete Job Route
@app.route("/delete/<int:job_id>")
@login_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted successfully!", "danger")
    return redirect(url_for("index"))


from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for("login"))
        
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid email or password. Please try again.", "danger")
    
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


