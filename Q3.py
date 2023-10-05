from flask import Flask
from datetime import datetime
# import class date time which have a function that return datetime
myapp_obj = Flask(__name__)

now =datetime.now()
#now call function datetime.now to get current date time

dt_string=now.strftime('%d-%m-%Y / %H:%M:%S')
#use strf convert date and time objects to string representation

@myapp_obj.route('/<subdirectory>')

def hello(subdirectory):
    
    return '''
    <html>
        <head>
            <title>Home Page - my blog</title>
        </head>
        <body>
            <h1>Hello, '''+subdirectory+'''</h1>
            <b> Today is '''+dt_string+'''</b>
        </body>
    </html>
'''
myapp_obj.run()









