from flask import Flask
#create an instance from flask class
#which imported from Flask library framework
myapp_obj = Flask(__name__)
#instantial object from flask class 
@myapp_obj.route('/hello')
#different URL the app will implement we set this page/hello

#create function to return string Hello which will appear on the page
def index():
    return "Hello World!"
myapp_obj.run()
#call the object that created from flask class with function run
#run function is enable flask to execute, webserver.

