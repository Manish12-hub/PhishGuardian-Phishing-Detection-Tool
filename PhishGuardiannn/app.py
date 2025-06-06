from flask import Flask, render_template, request
from detector import detect_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = detect_url(url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
