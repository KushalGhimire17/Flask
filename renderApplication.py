from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page of render application"

@app.route("/rend")
def index():
    return render_template("renderApp.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
