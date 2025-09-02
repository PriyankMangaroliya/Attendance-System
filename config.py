from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db_connection(app):
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/AttendanceSystem'
    mongo.init_app(app)

