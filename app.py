from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()

    if "hepsiburada.com" in incoming_msg:
        try:
            result = analyze_product_from_hepsiburada(incoming_msg)

            name = result['name']
            price = result['price']
            scores = result['scores']

            reply = f"📌 {name}\n💸 Fiyat: {price}\n\n"
            for key, val in scores.items():
                reply += f"✅ {key}: {val['value']}\n{val['note']}\n\n"

        except Exception as e:
            reply = f"Ürün analiz edilirken bir hata oluştu: {str(e)}"
    else:
        reply = "Lütfen Hepsiburada ürün linki gönderin."

    resp.message(reply)
    return str(resp)
