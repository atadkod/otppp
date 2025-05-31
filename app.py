from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from hosteller_api import get_room_otp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    print("hi")
    incoming_msg = request.form.get("Body").strip().lower()
    sender = request.form.get("From")

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "hi":
        otp_data = get_room_otp("6822fa45c3adf70d3dd83105")  # Replace with your dynamic booking ID logic
        if otp_data["success"]:
            msg.body(f"Your Room OTP is: {otp_data['roomOtp']}\nRoom No: {otp_data['roomNo']}")
        else:
            msg.body("Could not fetch OTP. Please try again later.")
    else:
        msg.body("Send 'hi' to get your room OTP.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False, port=5001)


