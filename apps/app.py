from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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


if __name__ == '__main__':
    app.run(debug=True)
