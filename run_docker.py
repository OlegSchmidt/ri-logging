"""
created at: 2018-12-19
author:     Volodymyr Biryuk

The module to run the micro service in a production environment (used by Docker).
"""
import os

import microservice


if __name__ == '__main__':
    app = microservice.create_app()
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dirname, 'coverage-reports')
    for file in os.listdir(filename):
        app.logger.info(file)
    app.run(host=app.config['MS_HOST'], port=int(app.config['MS_PORT']))
