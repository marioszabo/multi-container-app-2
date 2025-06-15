from flask import Flask

app = Flask(__name__)  # ✅ Correct

@app.route('/')
def hello():
    return "Hello from Flask backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

