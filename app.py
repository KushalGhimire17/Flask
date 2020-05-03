from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

""" single routes
@app.route("/kushal")
def kushal():
    return "<h1>Hello Kushal!</h1>"
"""

@app.route("/<string:name>")
def index1(name):
    name = name.capitalize()
    return "<h1>Hello {}!</h1>".format(name)


@app.route("/rend")
def index2():
    return render_template("indexRender.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
