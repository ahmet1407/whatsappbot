from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()

    if "hepsiburada.com" in incoming_msg:
        result = analyze_product_from_hepsiburada(incoming_msg)
        if "error" in result:
            reply = result["error"]
        else:
            scores = result["scores"]
            reply = f"📌 {result['name']}\n💸 {result['price']}\n\n✅ Tatmin: {scores['Satisfaction']['value']}\n🧯 Risk: {scores['Risk']['value']}\n💠 Hissiyat: {scores['Feel']['value']}\n⚙️ Uzman Testi: {scores['Expert Test']['value']}\n\nNotlar:\n- {scores['Satisfaction']['note']}\n- {scores['Risk']['note']}\n- {scores['Feel']['note']}\n- {scores['Expert Test']['note']}"
    else:
        reply = "Lütfen geçerli bir Hepsiburada ürün linki gönderin."

    resp.message(reply)
    return str(resp)
