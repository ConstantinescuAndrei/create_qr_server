import qrcode
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/create-qr', methods=['POST'])
def create_qr():
    payload = request.get_json()

    if request.method == 'POST':
        print(payload['menu_link'])
        menu_link = payload['menu_link']
        img = qrcode.make("www.google.com/" + menu_link)
        img.save("qrcode.png")

        return send_file('qrcode.png')

    return 'bad rerquest!', 400

if __name__ == '__main__':
    app.run(debug=True)


