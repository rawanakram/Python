from flask import Flask 
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!!!'


@app.route('/dojo') 
def dojo():
    return 'Dojo'


@app.route('/say/<name>') 
def say_hello(name):
    print("in the say_hello function")
    return f"Hi {name}"


@app.route('/repeat/<int:num>/<name>') 
def repeat_word(num, name):
    return name*num


@app.route('/success')
def success():
  return "success"

   
if __name__=="__main__":     
    app.run(debug=True)