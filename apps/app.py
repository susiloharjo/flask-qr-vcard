from flask import Flask, render_template,request
import qrcode
import os
from flask import current_app


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/namecard")
def namecard():
    return render_template("namecard.html")

@app.route("/wificard")
def wificard():
    return render_template("wificard.html")


@app.route("/barcode", methods=["POST"])

def generate_vcard():
    # fn = "John Doe"
    # org = "Company Name"
    # tel = "+123456789"
    # email = "john@example.com"
    fn = request.form.get("name")
    org = request.form.get("company")
    tel = request.form.get("phone_number")
    email = request.form.get("email")



    vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{fn}
ORG:{org}
TEL:{tel}
EMAIL:{email}
END:VCARD
    """

    return render_template('vcard_template.html', vcard_data=vcard_data)

@app.route("/wifi", methods=["POST"])

def generate_card():
    ssid = request.form.get("name")
    password = request.form.get("password")
    image = "wifi_qr.png"
    
    wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    # img.filename = "wifi_qr.png"
    # Save to templates/img 
    img_path = os.path.join(current_app.root_path, 'static/img', image)
    img.save(img_path)

    return render_template('wifi_template.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5300, debug=True)

