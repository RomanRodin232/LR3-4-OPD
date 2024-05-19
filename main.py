from flask import Flask, render_template, request
from reshenie import reshenie
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def ovtet():
    if request.method == 'POST':
        a = float(request.form.get ('a'))
        b = float(request.form.get ('b'))
        c = float(request.form.get ('c'))
    return render_template("index.html", answer = reshenie(a,b,c))

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True)