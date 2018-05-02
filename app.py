from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def handler():
    print(request.form.get('text'))
    return 'Success!'

if __name__ == "__main__":
    app.run()
