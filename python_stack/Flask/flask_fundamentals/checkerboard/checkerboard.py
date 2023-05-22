from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')
@app.route('/<int:y>')
@app.route('/<int:y>/<int:x>')
def index2(y = 8, x = 8):
    return render_template("index.html", num1=y, num2=x)


if __name__=="__main__":
    app.run(debug=True) 