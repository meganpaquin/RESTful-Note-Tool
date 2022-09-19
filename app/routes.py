from flask import (Flask, render_template, request, redirect)

app = Flask(__name__)
from app.database import notes

DATA = {
    "Status" : "Success"
}

@app.get("/")
def index():
    response = dict(DATA)
    response["all_notes"] = notes.scan()
    scan_data = response.get("all_notes")
    return render_template("index.html", data=scan_data)


@app.post("/notes")
def create_note():
    form_data = request.form
    new_dict = {
        "title" : form_data.get("title"),
        "subtitle" : form_data.get("subtitle"),
        "body" : form_data.get("body")
    }
    notes.create(new_dict)
    return redirect('/')

@app.get("/notes")
def get_notes():
    response = dict(DATA)
    response["all_notes"] = notes.scan()
    scan_data = response.get("all_notes")
    return scan_data

@app.get("/note/bytitle/<key>")
def get_note_by_title():
    pass

# This works currently
@app.get("/note/<key>")
def get_one_note(key):
    scan_data = notes.select_by_id(key)
    return render_template("single_note.html", data=scan_data)

# I have no idea why this works like this....
@app.post("/note/yes/<key>")
def update_note(key):
    form_data = request.form
    new_dict = {
        "title" : form_data.get("title"),
        "subtitle" : form_data.get("subtitle"),
        "body" : form_data.get("body")
    }
    notes.update(new_dict, key)
    return redirect("/")

# This works currently
@app.get("/note/del/<key>")
def delete_one_note(key):
    scan_data = notes.select_by_id(key)
    return render_template("delete_note.html", data=scan_data)

# WHY DOES THIS WORK WITH A GET REQUEST AND NOT A DELETE REQUEST!!!!!! 
@app.get("/note/del/yes/<key>")
def delete_note(key):
    scan_data = notes.delete(key)
    return redirect("/")