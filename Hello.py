from flask import FLASK
app=FLASK(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__=='___main__':
    app.run()



