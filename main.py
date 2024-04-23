from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/work1')
def work1():
    return render_template('work1.html')

@app.route('/work2')
def work2():
    return render_template('work2.html')

app.add_url_rule('/', 'index', index)
app.add_url_rule('/about', 'about', about)
app.add_url_rule('/work1', 'work1', work1)
app.add_url_rule('/work2', 'work2', work2)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, host="0.0.0.0")