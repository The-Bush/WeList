import sqlite3
from flask import redirect, session, url_for
from functools import wraps

def create_db_connection():
    """Begin a transaction, returns a cursor and connection"""
    connection = sqlite3.connect('lists.db')
    cursor = connection.cursor()
    return connection,cursor


def session_required(f):
    """
    Decorate routes to require a list to be selected.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('list_id') is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

def generate_referral(list_id, list_name):
    url = url_for('referral', list_id=list_id, list_name=list_name, _external=True)
    return url

def remove_list(list_id):
    connection, db = create_db_connection()
    db.execute('DELETE FROM items WHERE list_id = ?', (list_id, ))   
    db.execute('DELETE FROM lists WHERE id = ?', (list_id, ))
    connection.commit()
    connection.close()


def usd(value):
    """Format value as USD."""
    if value % 1 == 0.0:
        return f"${value:,.0f}"
    else:
        return f"${value:,.2f}"
    
