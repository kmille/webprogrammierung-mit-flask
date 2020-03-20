#!/usr/bin/env python3
import zulip
from flask import Flask, render_template, request

app = Flask(__name__)


client = zulip.Client()


@app.route("/test")
def view_test():
    return "hi ho"


@app.route("/")
def index():
    return render_template("notify-formular.html")


@app.route("/template-test")
def template_test():
    variable = "das ist eine python variable"
    return render_template("template-beispiel.html", variable=variable)


@app.route("/send-nachricht", methods=['GET', 'POST'])
def send_nachricht():
    user_message = request.form['nachricht']
    nachricht = "@**kmille**" + " Test nachricht von der api - sry nochmal: " + user_message
    message = {
      "type": "stream",
      "to": 'remote',
      "subject": "Anti-Überwachungs-Router",
      "content": "{}".format(nachricht),
    }
    client.send_message(message)
    return "Nachricht wurde gesendet"


@app.route("/members")
def list_members():
    members = client.get_members()['members'][390:500]
    return render_template("members.html", members=members)



if __name__ == '__main__':
    app.run(debug=True)
