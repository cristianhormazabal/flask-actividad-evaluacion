from flask import Flask, render_template, request

app = Flask(__name__)


def formatear_peso_chileno(valor):
    return f"${int(valor):,}".replace(",", ".")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': formatear_peso_chileno(total_sin_descuento),
            'total_con_descuento': formatear_peso_chileno(total_con_descuento),
            'descuento': int(descuento * 100)
        }
    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
