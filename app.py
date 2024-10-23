from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
# Necesario cuando se usa sesion
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
  if 'datos' not in session:
    session['datos'] =[]    #Inicializando para almacenar datos
  return render_template('index.html')

@app.route('/lista')
def lista():
  return render_template('lista.html', datos=session['datos'])

@app.route('/verificar', methods=['GET', 'POST'])
def verificar():
  if 'id' not in session:
      session['id'] = 0
  session['id'] += 1
  
  id = session['id']  # Asigna el valor a la variable local id
  fecha = request.form.get('fecha')
  nombre = request.form.get('nombre')
  apellido = request.form.get('apellido')
  turno = request.form.get('turno')
  seminario = request.form.getlist('seminario[]')
  seminarios_str = ', '.join(seminario)
  if 'datos' not in session:
    session['datos'] =[]
  session['datos'].append({'id':id,'fecha':fecha,'nombre':nombre,'apellido':apellido,'turno':turno,'seminario':seminarios_str})
  session.modified=True
  print(session['datos'])
  return redirect(url_for('index'))
  
@app.route('/vaciar')
def vaciar():
  # Eliminanos la sesion
  session.pop("datos", None)
  return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    # Lógica para editar el registro con el id correspondiente
    return f'Editar registro con ID: {id}'

@app.route('/borrar/<int:id>')
def borrar(id):
    # Lógica para borrar el registro con el id correspondiente
    return redirect(url_for('index'))



if __name__ == '__main__':
  app.run(debug=True)