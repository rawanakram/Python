from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def Index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    fav_language_from_form = request.form['fav_language']
    comment_from_form = request.form['comment']
    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form, 
                           fav_language_on_template=fav_language_from_form, comment_on_template=comment_from_form)


if __name__ == "__main__":
    app.run(debug=True)