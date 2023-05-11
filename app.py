from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # Check that username and password are correct and then sets current user
        handle = request.form["username"]
        password = request.form["password"]
        if db_session.query(Voter).where((Voter.username == handle) & (Voter.password == password)).first() != None:
            session["username"] = handle
            return redirect(url_for("home"))
        else:
            flash("Incorrect username or password", "error")
            return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        # Checks that user entered password correctly and that username is not taken,
        # then creates new user and sets them to current user
        handle = request.form["username"]
        password = request.form["password"]
        check = request.form["check"]
        if password != check:
            flash("Passwords do not match", "error")
            return render_template("signup.html")
        else:
            if db_session.query(Voter).where(Voter.username == handle).count() == 0:
                newuser = Voter(username=handle, password=password)
                db_session.add(newuser)
                db_session.commit()
                session["username"] = handle
                return redirect(url_for("home"))


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        results = db_session.query(Food).all()
        return render_template("home.html", results=results)
    else:
        # Check that user entered valid food and then add vote for that food
        foodname = request.form["vote"]
        current_username = session["username"]
        if db_session.query(Food).where(Food.name == foodname).first() != None:
            # create new vote for Food
            newvote = Vote(voter_id=current_username, food_name=foodname)
            db_session.add(newvote)
            db_session.commit()
            return redirect(url_for("home"))
        else:
            results = db_session.query(Food).all()
            return render_template("home.html", results=results)
        # reset votes
        # reset = db_session.query(Vote).all()
        #     db_session.delete(results)
        #     db_session.commit()


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        results = db_session.query(Food).all()
        return render_template("admin.html", results=results)
    else:
        # Allow user to create new food item, checks that item does not already exist
        foodname = request.form["create"]
        genrename = "all"
        if db_session.query(Food).where(Food.name == foodname).count() == 0:
            newfood = Food(name=foodname, genre=genrename)
            db_session.add(newfood)
            db_session.commit()
            flash("Item is now created", "error")
            results = db_session.query(Food).all()
            return render_template("admin.html", results=results)
        else:
            flash("Item with that name already exists", "error")
            results = db_session.query(Food).all()
            return render_template("admin.html", results=results)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5002)
