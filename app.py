from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada
import os

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()

    if "hepsiburada.com" in incoming_msg:
        try:
            result = analyze_product_from_hepsiburada(incoming_msg)
            name = result["name"]
            price = result["price"]
            scores = result["scores"]

            reply = f"""📌 {name}
💸 {price}

✅ Tatmin: {scores['Satisfaction']['value']}/100
{scores['Satisfaction']['note']}

🧯 Risk: {scores['Risk']['value']}/100
{scores['Risk']['note']}

💠 Hissiyat: {scores['Feel']['value']}/100
{scores['Feel']['note']}

⚙️ Uzman Testi: {scores['Expert Test']['value']}
{scores['Expert Test']['note']}"""
        except Exception as e:
            reply = f"Ürün verileri alınırken hata oluştu: {e}"
    else:
        reply = "Lütfen geçerli bir Hepsiburada ürün linki gönderin."

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
