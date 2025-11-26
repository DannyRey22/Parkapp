from flask import Flask, render_template, request, redirect, url_for
from utils.excel_manager import (
    leer_parques,
    agregar_parque,
    obtener_parque_por_id,
    editar_parque,
    eliminar_parque
)

app = Flask(__name__, template_folder='Mi_Parque', static_folder='static')

 
#   RUTA PRINCIPAL
 
@app.route("/")
def inicio():
    return render_template("index.html")


 
#   LISTAR PARQUES
 
@app.route("/parques")
def listar_parques():
    df = leer_parques()
    parques = df.to_dict(orient="records")
    return render_template("listar_parques.html", parques=parques)


 
#   AGREGAR PARQUE
 
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        datos = {
            "Nombre": request.form["nombre"],
            "Localidad": request.form["localidad"],
            "Direccion": request.form["direccion"],
            "Tamano_m2": request.form["tamano"],
            "Tipo": request.form["tipo"],
            "Estado": request.form["estado"],
            "Canchas": request.form["canchas"],
            "Juegos": request.form["juegos"],
            "Ultimo_mantenimiento": request.form["mantenimiento"]
        }
        agregar_parque(datos)
        return redirect(url_for("listar_parques"))

    return render_template("agregar_parque.html")


 
#   EDITAR PARQUE
 
@app.route("/editar/<int:id_parque>", methods=["GET", "POST"])
def editar(id_parque):
    if request.method == "POST":
        datos_modificados = {
            "Nombre": request.form["nombre"],
            "Localidad": request.form["localidad"],
            "Direccion": request.form["direccion"],
            "Tamano_m2": request.form["tamano"],
            "Tipo": request.form["tipo"],
            "Estado": request.form["estado"],
            "Canchas": request.form["canchas"],
            "Juegos": request.form["juegos"],
            "Ultimo_mantenimiento": request.form["mantenimiento"]
        }
        editar_parque(id_parque, datos_modificados)
        return redirect(url_for("listar_parques"))

    parque = obtener_parque_por_id(id_parque)
    return render_template("editar_parque.html", parque=parque)


 
#   ELIMINAR PARQUE
 
@app.route("/eliminar/<int:id_parque>")
def eliminar(id_parque):
    eliminar_parque(id_parque)
    return redirect(url_for("listar_parques"))


 
#   EJECUTAR APP
 
if __name__ == "__main__":
    app.run(debug=True)
