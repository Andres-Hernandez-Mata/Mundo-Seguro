from flask import Flask, render_template 
app = Flask(__name__) 

@app.route("/") 
def freezer(): 
    return render_template("basta.html")

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port = 5000, debug = True)



