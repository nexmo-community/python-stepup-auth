# server.py

from flask import Flask, render_template, session, request
import os
from os.path import join, dirname
from dotenv import load_dotenv
from vonage import Client, Verify

dotenv_path = join(dirname(__file__), "../.env")

app = Flask(__name__)
app.config["SECRET_KEY"] = "VonageVerify"

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME")

client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
verify = Verify(client)

global verify_number


@app.route("/")
def index():
    registered_number = None
    if "verified_number" in session:
        registered_number = session["verified_number"]
    return render_template("index.html",
                           number=registered_number,
                           brand=VONAGE_BRAND_NAME)


@app.route("/authenticate")
def authenticate():
    return render_template("authenticate.html")


@app.route("/verify", methods=["POST"])
def verify_user():
    session["unverified_number"] = request.form.get("mobile_number")
    response = verify.start_verification(number=session["unverified_number"],
                                         brand=VONAGE_BRAND_NAME)
    session["request_id"] = response["request_id"]
    print("Request ID: %s" % response["request_id"])

    if response["status"] == "0":
        return render_template("entercode.html")
    else:
        return render_template("index.html", error=response["error_text"])


@app.route("/check-code", methods=["POST"])
def check_code():
    response = verify.check(session["request_id"],
                            code=request.form.get("code"))

    if response["status"] == "0":
        session["verified_number"] = session["unverified_number"]
        return render_template("index.html",
                               number=session["verified_number"],
                               brand=VONAGE_BRAND_NAME)
    else:
        return render_template("index.html", error=response["error_text"])


@app.route("/logout")
def cancel():
    session.pop("verified_number", None)
    return render_template("index.html", brand=VONAGE_BRAND_NAME)


# run the server
if __name__ == "__main__":
    app.run(debug=True)
