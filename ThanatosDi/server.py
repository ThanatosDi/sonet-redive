from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return str(request.values)

if __name__ == "__main__":
    app.run(debug=True)