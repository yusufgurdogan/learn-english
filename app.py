from flask import Flask
from flask import render_template, redirect, url_for, request, abort, flash, session
app = Flask(__name__, static_url_path="", static_folder="static")
import random
import questions

@app.route('/')
def start():
	global getList
	getList = questions.myList
	randomNumber = random.randint(0,16)
	theQuestion = getList[randomNumber]["question"]
	global questionNumber #doeweneedd
	questionNumber = getList[randomNumber]["number"]
#	theAnswer = getList[randomNumber]["answer"]
	return render_template('start.html', Question = theQuestion)

@app.route('/check', methods=['POST'])
def redirectimento():
	complete_address = '/answer/' + str(questionNumber)
	return redirect(complete_address)

@app.route('/answer/<questionNumberr>')
def showAnswer(questionNumberr = None):
	return render_template('answer.html', Answer = getList[questionNumber]["answer"])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='1234')
