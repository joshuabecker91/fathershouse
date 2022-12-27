from flask import render_template, redirect, session, request, flash
from flask_app import app

# -----------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
