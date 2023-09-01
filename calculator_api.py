from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to check if the service is available
@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return jsonify({'message': 'Hello world!'})

# Endpoint to add two numbers
@app.route('/calculator/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first + second
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Invalid request data'}), 400

# Endpoint to subtract two numbers
@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first - second
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Invalid request data'}), 400

if __name__ == '__main__':
    app.run(debug=True)

