from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Permite que el HTML pueda llamar a la API
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="taller"
    )

# GET - Devuelve todos los vehículos
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()
    db.close()
    return jsonify(vehicles)

# POST - Crea una nueva cita
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO cites (vehicle_id, data_cita, servei_sollicitat) VALUES (%s, %s, %s)",
        (data['vehicle_id'], data['data_cita'], data['servei_sollicitat'])
    )
    db.commit()
    db.close()
    return jsonify({'message': 'Cita creada'}), 201

# GET - Devuelve todas las citas
@app.route('/appointments', methods=['GET'])
def get_appointments():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT cites.id, vehicles.matricula, vehicles.model, 
               cites.data_cita, cites.servei_sollicitat
        FROM cites
        JOIN vehicles ON cites.vehicle_id = vehicles.id
    """)
    appointments = cursor.fetchall()
    db.close()
    return jsonify(appointments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)