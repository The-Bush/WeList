# [WeList](https://welist.onrender.com/)
### Video Demo: https://www.youtube.com/watch?v=WPt_91qdXu0
### Description:
WeList is a grocery list making/sharing web app where a person can easily create a shopping list and share it with their friends and family by sharing a link or list name and password. Too many apps exist that require logins and various forms of authentication to access simple, shared content. With WeList, I wanted to prototype something that gets around that frustration and makes sharing easy. A good comparison would be pastebin, but formatted to specifically support shopping lists.


## Languages, Libraries and Frameworks:
* Python
    - sqlite3
    - Flask
    - Flask_Session
    - Werkzeug
    - Jinja2
    - Gunicorn
* HTML
* CSS
* JavaScript
* Bootstrap


## app.py

App.py is the main flask app file. It handles all of the interactions the user has with the website including accessing, creating, and modifying lists by interacting with the database.

## modules.py

This includes some helper functions that aren't directly related to website interactions, so I chose to abstract them to their own seperate .py file. These include a function for establishing transactions with the database, one for deleting lists, and others.

## listscripts.js

This .js file is specifically used on the listview page. It enables me to hide and un-hide the delete button based on if a user has hovered their mouse/tapped on the row they wish to delete. It also enables the user to copy a shareable link to their clipboard.

## styles.css

Contains only a few classes. One for the "hidden" buttons, and one for the appearance of the trash icon.

## layout.html

All other .html pages extend layout.html

The main feature of layout.html is the included navbar. This navbar is taken from the [bootstrap docs](https://getbootstrap.com/docs/5.3/components/navbar/) and modified to have links to different pages of the website.

## home.html, createlist.html, viewlist.html

These are the html templates that facilitate all of the interactions with the server.
home.html is where users will search and access an existing list.
createlist.html self explanatory.
viewlist.html will read and output all of the contents of the list for the user to view and modify (only adding and deleting items is supported)

## lists.db

This database includes two tables, one for storing list names and passwords, and another for storing items. The items table is indexed for faster searching based on the list_id.

```
CREATE TABLE sqlite_sequence(name,seq);

CREATE TABLE lists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password_hash TEXT,
    last_used TEXT NOT NULL);

CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    qty INTEGER,
    cost_each NUMERIC,
    FOREIGN KEY(list_id) REFERENCES lists(id));

CREATE INDEX item_index ON items (list_id);
```
