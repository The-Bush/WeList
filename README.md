# WeList
### Video Demo:
### Description:
WeList is a list making/sharing web app where a person can easily create a list and share it with their friends and family by sharing a link OR list name and password. Too many apps exist that require logins and various forms of authentication to access simple, shared content. With WeList, I wanted to protype out something that gets around that frustration and makes sharing easy and accessible.

## Languages, Libraries and Frameworks:
* Python
    - sqlite3
    - bcrypt
    - Flask
    - Flask
    - Jinja2

* HTML
* CSS
* JavaScript
* Bootstrap

### layout.html
All other .html pages extend layout.html

The main feature of layout.html is the included navbar. This navbar is taken straight from the [bootstrap docs](https://getbootstrap.com/docs/5.3/components/navbar/) and modified to have links to different pages of the website.

### home.html, createlist.html, viewlist.html



# TODO:
* Create modern, mobile friendly layout
    - Modularity not too important since interface will be very simple
    - Some AI-Generated Logos could be cool

* Create sqlite3 database
    - Table to store list id's and attributes (password, date-time, type (gift, grocery, wish), etc).
    - Table to store items in list 

* Create automated database management
    - Script that checks the last viewed date of a list, and deletes it if it is beyond a certain range. This ensures the database remains 
    - On/Off switch for this to only turn it on if needed (if somehow this thing takes off)


* Create homepage to create or access an existing list
* List modification page
    - Add items (name, price, qty)
    - Remove items
    - Modify qty
    - Search items to add(?)
    - GPT integration to suggest recipes based on the shopping list

* Share button that shares a link that posts directly to the list

* AI suggested recipes based on items in the list.