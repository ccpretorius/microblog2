"""
Micro BLOG settings for riaanpret1 project.

using FLASK.

For more information on this file, CONTACT ME HERE 
https://www.fiverr.com/riaanpret1

"""

import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Application definition


def create_app():
    app = Flask(__name__)
    client = MongoClient(
        "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.udnrr.mongodb.net/microblog?retryWrites=true&w=majority")
    app.db = client.microblog

    # Database MONGO

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert(
                {"content": entry_content, "date": formatted_date})

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(
                    entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        entries_with_date.reverse()

        return render_template("home.html", entries=entries_with_date)

    return app
