from flask import Flask, render_template, request, make_response
app = Flask(__name__)

mensajes = []

@app.route("/")
def form():
    return render_template("mensaje.html")

# Vulnerable a XSS
@app.route("/mensaje_inseguro", methods=['GET', 'POST'])
def mensaje_inseguro():
    if request.method == "POST":
        msj = request.form["mensaje"]
        mensajes.append(msj)
        html = "<title> Aqui está tus mensajes </title>"
        for msj in mensajes:
            html = html + "<h1>" + msj + "</h1>"
            html = html + "<a href='" + msj + "'>&#128147;</a>"
    return html

# XSS mitigado usando Jinja2
@app.route("/mensaje_seguro", methods=['GET', 'POST'])
def mensaje_seguro():
    if request.method == "POST":
        msj = request.form["mensaje"]
        mensajes.append(msj)
    response = make_response(render_template("mis_mensajes.html", mensajes=mensajes))
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 5000, debug = True)



