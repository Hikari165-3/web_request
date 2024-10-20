from flask import Flask, render_template,request,redirect,url_for
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inscripciones")
def inscripciones():
    return render_template("form_inscripcion.html")

@app.route("/registro_libro")
def registro_libro():
    return render_template("form_regis_libro.html")
@app.route("/registro_usuario")
def registro_usuario():
    return render_template("form_regis_usuario.html")

@app.route("/registro_producto")
def registro_producto():
    return render_template("form_regis_producto.html")


@app.route("/proceso_inscripcion", methods=['POST'])
def proceso_inscripcion(): 
    nombre=request.form.get('nombre')
    apellidos=request.form.get('apellidos')
    curso=request.form.get('curso')
    return render_template("salida.html",nombre=nombre,apellidos=apellidos,curso=curso)

@app.route("/proceso_registro_usuario", methods=['POST'])
def proceso_registro_usuario(): 
    nombre=request.form.get('nombre')
    apellidos=request.form.get('apellidos')
    correo=request.form.get('correo')
    contrasena=request.form.get('contrasena')
    return render_template("salida.html",nombre=nombre,apellidos=apellidos,correo=correo,contrasena=contrasena)

@app.route("/proceso_registro_producto", methods=['POST'])
def proceso_registro_producto(): 
    producto=request.form.get('producto')
    categoria=request.form.get('categoria')
    existencia=int(request.form.get('existencia'))
    precio=float(request.form.get('precio'))
    return render_template("salida.html",producto=producto,categoria=categoria,existencia=existencia,precio=precio)

@app.route("/proceso_registro_libro", methods=['POST'])
def proceso_registro_libro(): 
    titulo=request.form.get('titulo')
    autor=request.form.get('autor')
    resumen=request.form.get('resumen')
    medio=request.form.get('medio')
    return render_template("salida.html",titulo=titulo,autor=autor,resumen=resumen,medio=medio)
    
if __name__=="__main__":
    app.run(debug=True, port='5017')