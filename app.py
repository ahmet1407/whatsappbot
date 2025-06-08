from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import generate_scorecard

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    if incoming_msg.startswith("scorecard "):
        product_query = incoming_msg.replace("scorecard ", "").strip()
        reply = generate_scorecard(product_query)
    else:
        reply = "Lütfen 'Scorecard Dyson süpürge' gibi bir ürün adı gönderin."

    resp.message(reply)
    return str(resp)
