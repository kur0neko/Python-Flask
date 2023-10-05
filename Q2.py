from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route('/<subdirectory>')

def index(subdirectory):
    return subdirectory
myapp_obj.run()

