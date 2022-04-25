#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/How To Play")
def Bio_Pages():
    return render_template("hwt.html")

@app.route("/Group")
def Group():
    return render_template("Group.html")

@app.route("/Play the Game")
def play():
    return render_template("ptg.html")


@app.route("/Process")
def Process():
    return render_template("Process.html")

if __name__ == "__main__":
    app.run()
