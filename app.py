from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_by_product_name

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    if incoming_msg:
        result = analyze_by_product_name(incoming_msg)
        reply = (
            f"📌 {result['name']}\n"
            f"💸 {result['price']}\n\n"
            f"✅ Tatmin: {result['scores']['Satisfaction']['value']}\n"
            f"{result['scores']['Satisfaction']['note']}\n\n"
            f"🧯 Risk: {result['scores']['Risk']['value']}\n"
            f"{result['scores']['Risk']['note']}\n\n"
            f"💠 Hissiyat: {result['scores']['Feel']['value']}\n"
            f"{result['scores']['Feel']['note']}\n\n"
            f"🧪 Uzman Skoru: {result['scores']['Expert Test']['value']}\n"
            f"{result['scores']['Expert Test']['note']}"
        )
    else:
        reply = "Lütfen analiz etmem için bir ürün adı yaz."

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
