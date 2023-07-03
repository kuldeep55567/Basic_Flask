from flask import Flask, render_template, request

app = Flask(__name__)
data = {}


@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/greet/<username>")
def greet(username):
    return f"Hello, {username}!"


@app.route("/farewell/<username>")
def farewell(username):
    return f"Goodbye, {username}!"


@app.route("/create", methods=["GET", "POST"])
def create_entry():
    if request.method == "POST":
        key = request.form["key"]
        value = request.form["value"]
        data[key] = value
    return render_template("create.html")


@app.route("/read")
def read_entries():
    return render_template("read.html", data=data)


@app.route("/update", methods=["GET", "POST"])
def update_entry():
    if request.method == "POST":
        key = request.form["key"]
        if key in data:
            value = request.form["value"]
            data[key] = value
    return render_template("update.html")


@app.route("/delete", methods=["GET", "POST"])
def delete_entry():
    if request.method == "POST":
        key = request.form["key"]
        if key in data:
            del data[key]
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
