from flask import Flask , render_template , request

import Year as y

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def malaysia():
    if request.method == 'POST':
        tahun = request.form['tahun']
        tahun_pred = y.year_prediction(tahun)
        mp = tahun_pred

    return render_template("index.html")

# @app.route("/sub", methods = ['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['username']
    
#     return render_template("submit.html", n = name)

if __name__ == "__main__":
    app.run(debug=True)
