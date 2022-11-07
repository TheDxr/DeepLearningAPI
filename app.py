import os
import config

from flask import Flask
from flask_restful import Api

from views import *

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
api = Api(app)


api.add_resource(TestView, '/')
api.add_resource(MLView, '/model/train')
api.add_resource(Predict, '/model/predict')
api.add_resource(DataSet, '/dataset')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

