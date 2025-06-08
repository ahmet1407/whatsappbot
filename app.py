# app.py
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()

    if 'hepsiburada.com' in incoming_msg:
        result = analyze_product_from_hepsiburada(incoming_msg)
        reply = f"\n\n📄 {result['name']}\n💸 {result['price']}\n"
        for key, value in result['scores'].items():
            reply += f"\n**{key}:** {value['value']}\n{value['note']}\n"
    else:
        reply = "Lütfen Hepsiburada'dan geçerli bir ürün linki gönderin."

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
