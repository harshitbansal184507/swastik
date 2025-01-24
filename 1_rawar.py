
from flask import *
from flask import Flask
import datetime
import hashlib
from Session21C import MongoDBHelper
from bson.objectid import ObjectId

web_app = Flask("event Management App")

# Create the Object of Flask
# Which represents a Web Application

db_helper = MongoDBHelper()

@web_app.route("/") # Decorator
def index():
    return render_template("index.html")

@web_app.route("/contact")
def contact():
    return render_template("contact.html")

@web_app.route("/admin")
def admin():
    return render_template("signinadmin.html")

@web_app.route("/a_register")
def signupadmin():
    return render_template("signupadmin.html")

@web_app.route("/forgotpass")
def forgotpass():
    return render_template("forgotpassword.html")   

@web_app.route("/user")
def user():
    return render_template("signinmain.html")

@web_app.route("/addimg")
def addimg():
    return render_template('image.html')



@web_app.route("/profile")
def profile():
     if len(session["email"]) != 0:
        return render_template("profile.html", name=session["name"], email=session["email"])
     else:
        return redirect("/")

@web_app.route("/venue")
def venue():
    return render_template("venue.html")

@web_app.route("/registration")
def registration():
    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """user_data = {
        "user_email": session["email"]
    """

    db_helper.collection = db_helper.db["events"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("registration.html", events=result, 
                               name=session["name"], email=session["email"])

@web_app.route("/create_event")
def create_event():
    return render_template("createvent.html")

@web_app.route("/feed")
def feed():
    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """user_data = {
        "user_email": session["email"]
    """

    db_helper.collection = db_helper.db["events"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("feedback.html", events=result,
                               name=session["name"], email=session["email"])

@web_app.route("/aprofile")
def aprofile():
     if len(session["email"]) != 0:
        return render_template("a_profile.html", name=session["name"], email=session["email"])
     else:
        return redirect("/")

@web_app.route("/register")
def register():
    return render_template("signupmain.html")

@web_app.route("/home")
def home():
    return render_template("dashboard.html", name=session["name"], email=session["email"])

@web_app.route("/success")
def success():
    return render_template("success.html", name=session["name"], email=session["email"])

@web_app.route("/adashboard")
def adashboard():
    return render_template("a_dashboard.html")



@web_app.route("/error")
def error():
    name = session.get("name", "Guest")
    email = session.get("email", "N/A")
    return render_template("error.html", name=name, email=email)

@web_app.route("/logout")
def logout():
    session.clear()  # Clear all session data
    return redirect("/")

#-----------------------------------for user login and signup -------------------------------------------------
@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["users"]

    existing_user = db_helper.fetch({"email": user_data["email"]})
    if existing_user:
        return render_template("error.html", message="User already exists. Please log in.")

    result = db_helper.insert(user_data)
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]
    return render_template("dashboard.html", name=session['name'], email=session['email'])

@web_app.route("/fetch-user", methods=["POST"])
def feth_user_from_db():
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["users"]
    try:
        result = db_helper.fetch(query=user_data)
    except Exception as e:
        return render_template("error.html", message=f"Database error: {str(e)}")

    if result:
        user_data = result[0]
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("dashboard.html", name=session['name'], email=session['email'])
    else:
        return render_template("error.html", message="User Not Found. Please Try Again",
                               name=session.get("name", "Guest"), email=session.get("email", "N/A"))

#-------------------------for admin login and sign up-----------------------------------------------------------
@web_app.route("/add-admin", methods=["POST"])
def add_userr_in_db():
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["admins"]

    existing_user = db_helper.fetch({"email": user_data["email"]})
    if existing_user:
        return render_template("error.html", message="User already exists. Please log in.")

    result = db_helper.insert(user_data)
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]
    return render_template("a_dashboard.html", name=session['name'], email=session['email'])

@web_app.route("/a_fetch-user", methods=["POST"])
def fetch_user_from_db():
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["admins"]
    try:
        result = db_helper.fetch(query=user_data)
    except Exception as e:
        return render_template("a_error.html", message=f"Database error: {str(e)}")

    if result:
        user_data = result[0]
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("a_dashboard.html", name=session['name'], email=session['email'])
    else:
        return render_template("a_error.html", message="User Not Found. Please Try Again",
                               name=session.get("name", "Guest"), email=session.get("email", "N/A"))

#--------------------------add event-----------------------------------------------------------------------------

@web_app.route("/add-event", methods=["POST"])
def add_event_in_db():

    # Create a Dictionary with Data from HTML Register Form
    event_data = {
        "name": request.form["name"],
        "ename":request.form["ename"],
        "date": request.form["date"],
        "venue": request.form["venue"],
        "time": request.form["time"],
        "description":request.form["description"],
        "user_email": session['email'],
        "user_name": session['name'],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["events"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(event_data)
    return render_template("asuccess.html", message = "event uploaded Successfully",
                           name=session["name"], email=session["email"])

#----------------------------fetch events-----------------------------------------------------

@web_app.route("/fetch-event")
def fetch_event_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """user_data = {
        "user_email": session["email"]
    }"""

    db_helper.collection = db_helper.db["events"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("eventadmin1.html", events=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message=" No upcoming events",
                               name=session["name"], email=session["email"])
    
@web_app.route("/eventmain")
def fetch_events_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """user_data = {
        "user_email": session["email"]
    }"""

    db_helper.collection = db_helper.db["events"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("eventmain.html", events=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message=" No upcoming events",
                               name=session["name"], email=session["email"])
    

@web_app.route("/delete-event/<id>")
def delete_patient(id):
    print("event to be deleted:", id)
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["events"]
    db_helper.delete(query)
    return render_template("asuccess.html", message = "event Deleted Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/update/<id>")
def update_event(id):
    print("event to be updated:", id)
    
    # Save Patient ID in Session, which needs to be updated
    session["id"] = id
    
    # Fetch document from patient collection, where id matches
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["events"]
    
    # result is a list
    result = db_helper.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with patient id matching the one we have passed
    patient_doc = result[0]

    return render_template("updatevent.html",
                           name=session["name"], 
                           email=session["email"], 
                           event=patient_doc)

@web_app.route("/update-event", methods=["POST"])
def update_patient_in_db():

    # Create a Dictionary with Data from HTML Register Form
    new_event_data = {
        "name": request.form["name"],
        "ename":request.form["ename"],
        "date": request.form["date"],
        "venue": request.form["venue"],
        "time": request.form["time"],
        "description":request.form["description"],
        "user_email": session['email'],
        "user_name": session['name'],
        "created_on": datetime.datetime.now()
    }
    db_helper.collection = db_helper.db["events"]

    query = {"_id": ObjectId(session["id"])}
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.update(new_event_data, query)
    return render_template("asuccess.html", message = "event Updated Successfully",
                           name=session["name"], email=session["email"])

#------------------------------------------registrations--------------------------------------
@web_app.route("/add-register", methods=["POST"])
def add_register_in_db():

    # Create a Dictionary with Data from HTML Register Form
    event_data = {
        "ename":request.form["ename"],
        "phone":request.form["phone"],
        "pname":request.form["pname"],
        "email":request.form["email"],
        "user_email": session['email'],
        "user_name": session['name'],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["registrations"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(event_data)
    return render_template("success.html", message = "congratulations!.. your registeration is Successfully done!",
                           name=session["name"], email=session["email"])

@web_app.route("/fetch-register")
def fetch_register_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """ user_data = {
        "user_email": session["email"]
    }"""

    db_helper.collection = db_helper.db["registrations"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("registrations.html", registrations=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message=" No registrations ",
                               name=session["name"], email=session["email"])
#----------------------------------------feedbacks--------------------------------------

@web_app.route("/add-feedback", methods=["POST"])
def add_feed_in_db():

    # Create a Dictionary with Data from HTML Register Form
    event_data = {
        "eventname":request.form["eventname"],
        "name":request.form["name"],
        "email":request.form["email"],
        "feedback":request.form["feedback"],
        "rating":request.form["rating"],
        "user_email": session['email'],
        "user_name": session['name'],
        "created_on": datetime.datetime.now()
    }
    
    db_helper.collection = db_helper.db["feedbacks"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(event_data)
    return render_template("success.html", message = "thankss for rating us..!",
                           name=session["name"], email=session["email"])

@web_app.route("/analyse")
def fetch_feed_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    """user_data = {
        "user_email": session["email"]
    }
"""
    db_helper.collection = db_helper.db["feedbacks"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch()
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("vfeedbacks.html", feedbacks=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message=" No feedbacks ",
                               name=session["name"], email=session["email"])

def main():

    # In order to use Session Tracking, create a Secret Key
    web_app.secret_key = "doctors-app-key-v1"

    # Run the App infinitely, till user wont quite
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()