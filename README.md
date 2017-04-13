Installation
===========

1. git clone https://github.com/ginkooo/milodjango
Step 2 can be skipped, it's just for creating separate python environment
2. install and activate virtual env
	- pip install virtualenv
	- mkdir ~/envs
	- virtualenv ~/envs/milo
	- source ~/envs/milo/bin/activate
3. pip install -r requirements.txt
3. ./manage.py migrate
4. ./manage.py runserver

Sreens are in `/screens`
CSB is in `users.csv`

How to use it
=============

To populete db with some data run:

`./manage.py populatedb`

You have a few places to go:

* / - Displays users in a table
* /list - Same as '/'
* /view/1 - View user with id 1
* /edit/1 - Edit user with id 1
* /add - Add user
* /list/csv - Export all users to csv

What's done
===========

- Views with templates for: listing all users, viewing one, adding, editting
- Bootstrap and own styles.css added
- Custom template tags:
 * One displaying 'allowed' if user is over 13 years old, 'blocked' otherwise
 * Second displaying BizzFuzz string depending on random-generated number (Specific to every user)
- Exporting to CSV with a button
- If fatal error occurs, or there is some success information, user is redirected to the / and message is showed to him through message framework
- url resolve tests

What's not done
===============

- Site doesn't look perfect yet
- Human-friendly links for accessing views
- Can't export only a single user to CSV
- Not every function is test-covered
- No functional tests
