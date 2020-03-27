from flask import Flask, escape, request
from datetime import datetime
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/today')
def today():
    t = Template(open("today.html",mode="r").read())
    return t.render({"today":datetime.now()})

if __name__ =="__main__":
    app.run(host="0.0.0.0",debug=True)