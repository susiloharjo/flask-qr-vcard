import qrcode
import requests
from flask import Flask, render_template, request
import vcard

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barcode", methods=["POST"])
def barcode():
    global vcard

    name = request.form.get("name")
    company = request.form.get("company")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")

    vcard = vcard.VCard()
    vcard.add_name(name)
    vcard.add_organization(company)
    vcard.add_tel(phone_number)
    vcard.add_email(email)

    qrcode = qrcode.make(vcard.serialize(), encoding="utf-8", error_correction=qrcode.constants.ERROR_CORRECT_L)

    filename = "barcode.png"
    qrcode.save(filename)

    with open(filename, "rb") as f:
        encoded_image = f.read()
        base64_image = base64.b64encode(encoded_image)

    os.remove(filename)

    return {
        "image": base64_image.decode("utf-8"),
        "name": name,
        "company": company,
        "phone_number": phone_number,
        "email": email,
    }

if __name__ == "__main__":
    app.run(debug=True)
