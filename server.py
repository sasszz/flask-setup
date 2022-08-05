from flask import Flask, render_template

app = Flask(__name__)

# Prints Hello World to browser automatically
@app.route('/')
def hello_world():
    return 'Hello World!'

# Connects to index.html file
@app.route('/html')
def run_html():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
