import qrcode
from flask import Flask, send_file, request
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

@app.route('/create-qr', methods=['POST'])
def create_qr():
    payload = request.get_json()

    if request.method == 'POST':
        print(payload['menu_link'])
        menu_link = payload['menu_link']
        print(menu_link['name'])
        print(menu_link['id'])
        img = qrcode.make("http://localhost:3000/" + menu_link['name'] + '/' + menu_link['id'])
        img.save("qrcode.png")
        encoded = base64.b64encode(open("qrcode.png", "rb").read())

        return encoded

    return 'bad rerquest!', 400

if __name__ == '__main__':
    app.run(debug=True)


