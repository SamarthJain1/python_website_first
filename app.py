from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://whoanonymous2548:realestate122548@cluster0.o5udw94.mongodb.net/"
)

DB = client["Shopping"]["Products"]

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        DB.insert_one(dict(request.form))
        return redirect(url_for("home"))
    return render_template("index.html")


@app.route("/post-data")
def post_data():
    data = DB.find()
    return render_template("card.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
x``