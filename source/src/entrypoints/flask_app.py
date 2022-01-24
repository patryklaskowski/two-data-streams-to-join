from flask import Flask, request

from src import bootstrap
from src.domain import commands

app = Flask(__name__)
message_bus = bootstrap.bootstrap()

# curl -X POST -H "Content-Type: application/json" \
# -d '{"datetime":2, "person_id":8, "temperature": 36.6}' \
# http://localhost:5005/temperature
# curl -X GET http://localhost:5005/threads


@app.route('/health', methods=['GET'])
def health():
    return {'message': 'success'}, 200


@app.route('/threads', methods=['GET'])
def active_threads():
    command = commands.GetActiveThreadsNumber()
    number = message_bus.handle(command)
    return {'message': 'Check on threads successful',
            'Active threads': number}, 200


@app.route('/temperature', methods=['POST'])
def handle_temperature_data():

    if request.headers.get('Content-Type', None) != 'application/json':
        return {'message': 'Content-Type must be `application/json`.'}, 400

    try:
        command = commands.SendTemperatureData(
            request.json['datetime'], request.json['person_id'], request.json['temperature'],
        )
        message_bus.handle(command)
    except KeyError as e:
        return {'message': 'One or more arguments missing.', 'error': f'Missing `{str(e)}` argument'}, 400
    except Exception as e:
        return {'message': 'Internal Server Error.', 'error': repr(e)}, 500

    return {'message': f'Temperature `{request.json["temperature"]}` data received.'}, 200


@app.route('/humidity', methods=['POST'])
def handle_humidity_data():

    if request.headers.get('Content-Type', None) != 'application/json':
        return {'message': 'Content-Type must be `application/json`.'}, 400

    try:
        command = commands.SendTemperatureData(
            request.json['datetime'], request.json['person_id'], request.json['humidity'],
        )
        message_bus.handle(command)
    except KeyError as e:
        return {'message': 'One or more arguments missing.', 'error': f'Missing `{str(e)}` argument'}, 400
    except Exception as e:
        return {'message': 'Internal Server Error.', 'error': repr(e)}, 500

    return {'message': f'Humidity `{request.json["humidity"]}` data received.'}, 200
