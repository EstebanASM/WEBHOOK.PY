from flask import Flask, request, jsonify
import uuid  # Para generar IDs únicos

app = Flask(__name__)

# Lista para almacenar los datos enviados al webhook con un ID único
webhook_data_storage = []

# Ruta para manejar el webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Verificar si la solicitud tiene datos JSON
    if request.is_json:
        # Obtener los datos JSON del cuerpo de la solicitud
        data = request.get_json()
        
        # Generar un ID único para cada dato
        data_id = str(uuid.uuid4())
        data['id'] = data_id  # Añadir el ID al dato
        print(f"Received webhook data: {data}")
        
        # Guardar los datos en la lista
        webhook_data_storage.append(data)
        
        # Responder con un mensaje
        return jsonify({"message": "Webhook received and data stored successfully!", "data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

# Ruta para obtener todos los datos almacenados
@app.route('/webhook/data', methods=['GET'])
def get_webhook_data():
    return jsonify({"stored_data": webhook_data_storage}), 200

# Ruta para buscar un dato específico utilizando su ID
@app.route('/webhook/data/<data_id>', methods=['GET'])
def get_webhook_data_by_id(data_id):
    # Buscar el dato con el ID proporcionado
    data = next((data for data in webhook_data_storage if data['id'] == data_id), None)
    
    if data:
        return jsonify({"data": data}), 200
    else:
        return jsonify({"error": f"No data found with ID {data_id}"}), 404

# Ruta para eliminar un solo dato utilizando su ID
@app.route('/webhook/data/<data_id>', methods=['DELETE'])
def delete_webhook_data(data_id):
    # Buscar el dato con el ID proporcionado
    data_to_delete = next((data for data in webhook_data_storage if data['id'] == data_id), None)
    
    if data_to_delete:
        webhook_data_storage.remove(data_to_delete)  # Eliminar el dato
        return jsonify({"message": f"Data with ID {data_id} has been deleted successfully!"}), 200
    else:
        return jsonify({"error": f"No data found with ID {data_id}"}), 404

# Ruta para editar un dato utilizando su ID (PUT)
@app.route('/webhook/data/<data_id>', methods=['PUT'])
def update_webhook_data(data_id):
    # Buscar el dato con el ID proporcionado
    data = next((data for data in webhook_data_storage if data['id'] == data_id), None)
    
    if data:
        # Obtener los nuevos datos del cuerpo de la solicitud
        updated_data = request.get_json()
        
        # Actualizar los campos del dato (si se proporcionan nuevos valores)
        data.update(updated_data)
        
        return jsonify({"message": f"Data with ID {data_id} has been updated successfully!", "data": data}), 200
    else:
        return jsonify({"error": f"No data found with ID {data_id}"}), 404

# Iniciar el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
