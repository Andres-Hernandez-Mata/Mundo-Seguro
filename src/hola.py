from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return "<h1> Hola, mundo! </h1>"

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port = 5000, debug = True)


