#!/usr/bin/env python

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Virtual Directory REST Service Using Swagger'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
