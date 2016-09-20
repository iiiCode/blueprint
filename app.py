from flask import Flask
from ModularA.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix="/pages")

@app.route('/')
def index():
    return "<h1>Hello, world.</h1>"

@app.route("/<name>")
def show_name(name):
    return "Hello, " + name

if __name__ == "__main__":
    app.run(host="0.0.0.0")
