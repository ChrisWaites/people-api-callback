from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def receive_message():
    print(request.data)

if __name__ == "__main__":
    app.run()
