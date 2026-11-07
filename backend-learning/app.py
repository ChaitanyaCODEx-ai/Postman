from os import name

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My first backend is working!"

@app.route("/about")
def about():
    return "This is the about page of my first backend!"

@app.route("/contact")
def contact():
    return "Contact us at ABCD1234@gmail.com"

@app.route("/students")
def students():
    students = [
    {"name": "Aman", "age": 21},
    {"name": "Rahul", "age": 20},
    {"name": "Priya", "age": 22}
]
    return jsonify(students)


@app.route("/students/<int:student_id>")
def get_student(student_id):
    return f"Student ID: {student_id}"

@app.route("/search")
def search():
    name = request.args.get("name")
    if name:
        return f"Search results for: {name}"
    else:
        return "Please provide a name to search for."

if __name__ == "__main__":
    app.run(debug=True)