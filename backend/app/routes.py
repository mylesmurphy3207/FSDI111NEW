from flask import Flask  # from the flask module import the Flask class
from flask import render_template


from datetime import datetime
# Create an instance of the Flask class into the app (now an object)
# class is to object as blueprint is to house.
app = Flask(_name_)


# a decorator that allows us to map a route to a "view function"
@app.get("/aboutmi")
def index():  # flask calls functions mapped to a route "view functions"
    out = {  # flask will automatically convert dictionaries to json for convenience
        "first_name": "John",
        "last_name": "Doe",
        "hobbies": "Illustration",
        "is_active": True
    }
    return out  # if we wish to build a restful service, this is a good convention  to follow
    # as JSON is the norm for the morst RESTful services


@app.get("/about")
def about():
    time_stamp = datetime.now().strftime("%F %H:%M:%S") # %F stands for date
    return render_template("about.html", timestamp=time_stamp)