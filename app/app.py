import os
import datetime

from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from modules import (
    create_db_connection,
    session_required,
    remove_list,
    usd,
    generate_referral,
)

# Configure application
app = Flask("FinalProject")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Add usd filter to jinja
app.jinja_env.filters["usd"] = usd


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "access" in request.form:
            # Catch if list name is empty
            if not request.form.get("listname"):
                app.logger.error("All forms not complete")
                return "All forms not complete", 400

            # Catch if password was input
            if not request.form.get("password"):
                password = None
            else:
                password = request.form.get("password")

            listname = request.form.get("listname")

            # Fetch list from database
            connection, db = create_db_connection()
            rows = db.execute(
                "SELECT id, name, password_hash FROM lists WHERE name = ?", (listname,)
            )
            rows = rows.fetchone()
            app.logger.debug("Found List", rows)
            connection.close()

            # Check if the list exists
            if rows is None:
                return "Invalid list name"

            # If list has a password, check for match
            if rows[2] != None:
                if not check_password_hash(rows[2], password):
                    return "Invalid password"

            # Store the id and name of the accessed list
            session["list_id"] = rows[0]
            session["list_name"] = rows[1]
            return redirect("/viewlist")

        elif "create" in request.form:
            return redirect("/createlist")

    else:
        app.logger.info("New user accessed website")
        return render_template("home.html")


@app.route("/createlist", methods=["GET", "POST"])
def createlist():
    if request.method == "POST":
        # Handle missing entries
        if not request.form.get("listname"):
            app.logger.error("List requires a name")
            return "List Requires a name", 400

        # Handle mismatched passwords
        if request.form.get("password"):
            if request.form.get("password") != request.form.get("confirmation"):
                app.logger.error("Passwords do not match")

            else:
                password = request.form.get("password")

        listname = request.form.get("listname")

        # Hash password if present
        if "password" in locals():
            hashPassword = generate_password_hash(
                password, method="pbkdf2:sha256", salt_length=16
            )
        else:
            hashPassword = None

            # Store plaintext password for requesting the login page
            password = None

        # Ensure list name does not already exist in table and throw error if it does
        connection, db = create_db_connection()
        db.execute("SELECT id FROM lists WHERE name = ?", (listname,))
        rows = db.fetchall()
        if rows:
            connection.close()
            return "Error, listname already in use"

        # Insert new list into the database
        db.execute(
            "INSERT INTO lists (name, password_hash, last_used) VALUES(?, ?, ?)",
            (listname, hashPassword, datetime.datetime.now()),
        )
        connection.commit()
        list_id = db.lastrowid
        connection.close()

        # Send a login request to the login page
        session["list_id"] = list_id
        session["list_name"] = listname

        return redirect("/viewlist")

    else:
        return render_template("createlist.html")


@app.route("/viewlist", methods=["GET", "POST"])
@session_required
def viewList():
    app.logger.debug("Session ID is " + str(session["list_id"]))
    if request.method == "POST":
        return "how did you get here?"
    else:
        # Fetch item list from database
        connection, db = create_db_connection()
        rows = db.execute(
            "SELECT name, qty, cost_each, id FROM items WHERE list_id = ?",
            (session["list_id"],),
        )
        items = rows.fetchall()
        connection.close()

        totalcost = 0.0
        for item in items:
            totalcost += item[1] * item[2]

        # Get share link
        link = generate_referral(session["list_id"], session["list_name"])
        return render_template(
            "viewlist.html",
            listname=session["list_name"],
            items=items,
            totalcost=totalcost,
            link=link,
        )


@app.route("/add_item", methods=["GET", "POST"])
@session_required
def add_item():
    if request.method == "POST":
        itemName = request.form.get("name")
        qty = request.form.get("qty")
        costEach = request.form.get("costEach")

        if not itemName.strip() or not qty.strip():
            return "Error, no item name or quantity provided"

        if not costEach.strip():
            costEach = 0

        # Insert new item into table
        connection, db = create_db_connection()
        db.execute(
            "INSERT INTO items (list_id, name, qty, cost_each) VALUES(?, ?, ?, ?)",
            (session["list_id"], itemName, qty, costEach),
        )
        connection.commit()
        connection.close()

        return redirect("/viewlist")


@app.route("/remove_item", methods=["GET", "POST"])
@session_required
def remove_item():
    if request.method == "POST":
        itemid = request.form.get("item")
        connection, db = create_db_connection()
        db.execute("DELETE FROM items WHERE id = ?", (itemid,))
        connection.commit()
        connection.close()
        return redirect("/viewlist")


@app.route("/delete_list", methods=["GET", "POST"])
@session_required
def delete_list():
    if request.method == "POST":
        list_id = session["list_id"]

        # Delete all items from items table and list from lists table
        remove_list(list_id)

        session.clear()
        return redirect("/")


@app.route("/ref", methods=["GET"])
def referral():
    session.clear()
    session["list_id"] = request.args.get("list_id")
    session["list_name"] = request.args.get("list_name")
    return redirect("/viewlist")
