from flask import Flask, render_template, request, redirect, url_for, jsonify
# import queryite3
from dotenv import load_dotenv

app = Flask(__name__)

# Conexión queryite3
load_dotenv()  


@app.before_request
def before_request():
    print("Antes de la petición...")


@app.after_request
def after_request(response):
    print("Después de la petición")
    return response

@app.route('/')
def index():
    data = {
        'titulo': 'Consulta con GPT3',
        'Bienvenida': '¡Saludos!'
    }
    return render_template('index.html', data= data)

@app.route('/response/<consult>')
def response(consult):
    data = {
        'titulo': 'Respuesta',
        'consulta': consult
    }
    return render_template('response.html', data= data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'ok'

# @app.route('/cursos', methods=['POST'])
# def listar_cursos():
#     data = {}
#     try:
#         # conexion = request.get_json()

#         connection = queryite3.connect('./data/database.db')
#         cursor = connection.cursor()
#         query = "SELECT ..."
#         cursor.execute(query)
#         cursos = cursor.fetchall()
#         # print(cursos)
#         data['cursos'] = cursos
#         data['mensaje'] = 'Exito'
#     except Exception as ex:
#         data['mensaje'] = 'Error...'
#     return jsonify(data)

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)

