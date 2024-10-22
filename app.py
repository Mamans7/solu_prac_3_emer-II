from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
# Necesario cuando se usa sesion
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
  if 'datos' not in session:
    session['datos'] =[]    #Inicializando para almacenar datos
  return render_template('index.html', datos=session['datos'])

@app.route('/verificar', methods=['GET', 'POST'])
def verificar():
  fecha = request.form.get('fecha')
  nombre = request.form.get('nombre')
  apellido = request.form.get('apellido')
  turno = request.form.get('turno')
  seminario = request.form.getlist('seminario[]')
  seminarios_str = ', '.join(seminario)
  if 'datos' not in session:
    session['datos'] =[]
  session['datos'].append({'fecha':fecha,'nombre':nombre,'apellido':apellido,'turno':turno,'seminario':seminarios_str})
  session.modified=True
  print(session['datos'])
  return redirect(url_for('index'))
  
@app.route('/vaciar')
def vaciar():
  # Eliminanos la sesion
  session.pop("datos", None)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)