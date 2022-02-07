#! /usr/bin/env python
from flask import Flask, render_template
import json
from random import choice
from bs4 import BeautifulSoup
import requests

def BBC_News():
    url = "https://www.bbc.com"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    dic = [item 
       for item in soup.select(".media__summary")]

    elem = choice(dic)

    c = elem.select(".media__summary")

    return(elem)

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def random_question():
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    return choice(questions)

def check_answer(q_id, a_id):
    with open("questions.json", 'r') as f:
        questions = json.load(f)
    q = list(filter(lambda x: x["id"] == q_id, questions))[0]
    return q["correct"] == a_id



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html", question=random_question())

@app.route("/question2")
def question2():
    return render_template("question2.html", question=random_question())

@app.route("/bio")
def Bio_Pages():
    return render_template("bio.html")

@app.route("/Shivam")
def Shivam():
    return render_template("Shivam.html")

@app.route("/Liam")
def Liam():
    return render_template("Liam.html")

@app.route("/Stefan")
def Stefan():
    return render_template("Stefan.html")

@app.route("/Group")
def Group():
    return render_template("Group.html")

@app.route("/BBC")
def news():
    return render_template("BBC.html",bbc=BBC_News())

@app.route("/virus")
def virus():
    return render_template("virus.html")
@app.route("/answer/<int:question_id>/<int:answer_id>")
def answer(question_id, answer_id):
    correct = check_answer(question_id, answer_id)
    return render_template("answer.html", correct=correct)


if __name__ == "__main__":
    app.run()
