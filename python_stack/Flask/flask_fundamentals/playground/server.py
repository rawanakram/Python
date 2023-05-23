from flask import Flask, render_template  
app = Flask(__name__)                     

@app.route("/play")    
@app.route("/play/<int:x>")
@app.route("/play/<int:x>/<color>")                           
def playground(x=3, color="skyblue"):
    return render_template('index.html', num=x, color=color )
    
if __name__=="__main__":
    app.run(debug=True)                   

