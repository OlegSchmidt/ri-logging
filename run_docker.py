"""
created at: 2018-12-19
author:     Volodymyr Biryuk

The module to run the micro service in a production environment (used by Docker).
"""
import microservice


if __name__ == '__main__':
    app = microservice.create_app()
    app.run(host=app.config['MS_HOST'], port=9798)
