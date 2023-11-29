from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax_url')
def ajax_fun():
    return "hello from flask ajax"

if __name__=="__main__":
    app.run(debug=True)