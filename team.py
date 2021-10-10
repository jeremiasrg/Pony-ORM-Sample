from flask import Flask
import apm.apm_config
from flask import request

from elasticapm.contrib.flask import ElasticAPM

from orm import operations

import os

os.path.join("orm")

app = Flask(__name__)

app.config['ELASTIC_APM'] = apm.apm_config.config()

apm = ElasticAPM(app, logging=True)


@app.route('/team/getAll', methods=['GET'])
def getTeams():
    rt = operations.findAll()
    response = app.response_class(response=rt,
                                  status=200,
                                  mimetype='application/json')
    return response


@app.route('/team', methods=['POST'])
def createTeam():
    request_data = request.get_json()
    return operations.createTeam(request_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
