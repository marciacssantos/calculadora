from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")
# Por padrão os arquivos que vao ser
# renderizados ficam na pasta templates, caso não queira deixar nessa pasta é
# necessario passar o caminho da pasta em template_folder="", se for usar a
# template mesmo, deixar só (__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template('index.html')

    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):

            if (request.form["opc"] == "soma"):
                return str(int(request.form["num1"]) + int(request.form["num2"]))

            elif (request.form["opc"] == "subt"):
                return str(int(request.form["num1"]) - int(request.form["num2"]))

            elif (request.form["opc"] == "mult"):
                return str(int(request.form["num1"]) * int(request.form["num2"]))

            else:
                return str(int(request.form["num1"]) / int(request.form["num2"]))

        else:
            return "Preencha todos os campos"
# def home_id(id):
# return f"Olá {id}"


@app.errorhandler(404)  # Se tiver o erro 404
def not_found(error):
    return render_template("error.html")


app.run(port=5005, debug=True)
