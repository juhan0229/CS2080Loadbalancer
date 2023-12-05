
from flask import Flask, jsonify
import requests

app: Flask = Flask(__name__)

HOSTS = ['9c2b9f22-eb1b-44aa-91ed-2fad3abc42d2.mock.pstmn.io',
         '9c2b9f22-eb1b-44aa-91ed-2fad3abc42d2.mock.pstmn.io',
         'bad']
# PORTS = [None,
#          7000,
#          8080]
index = 0

@app.route('/darian', methods=['GET'])
def route():
    success = False
    attempt = 0
    response = {'success': 'FAILED'}

    while not success and attempt < 3:
        try:
        # Pick server
            global index
            host = HOSTS[index]
            # port = PORTS[index]
            index += 1
            if index >= len(HOSTS):
                index = 0

            # Forward request to that server
            # port_str = f':{port}' if port else ''
            port_str = ''
            full_response = requests.get(url=f'http://{host}{port_str}', timeout=1)
            response = full_response.text
            success = True
            print(f'Success on {host}{port_str}!')
        except:
            print(f'Uh oh - Failed on {host}{port_str}')

        attempt += 1

    # Return response from other server
    return jsonify(response)
