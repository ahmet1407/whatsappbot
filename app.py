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
            name = result["name"]
            price = result["price"]
            scores = result["scores"]

            response_text = f"""
📌 *{name}*
💸 *Fiyat:* {price}

### Skorlar (100 üzerinden)

✅ *Tatmin:* {scores['Satisfaction']['value']}
_{scores['Satisfaction']['note']}_

🧯 *Risk:* {scores['Risk']['value']}
_{scores['Risk']['note']}_

💠 *Hissiyat:* {scores['Feel']['value']}
_{scores['Feel']['note']}_

⚙️ *Uzman Skoru:* {scores['Expert Test']['value']}
_{scores['Expert Test']['note']}_
"""
            resp.message(response_text)
        except Exception as e:
            resp.message("Üzgünüm, ürün verisini işlerken bir hata oluştu. Lütfen geçerli bir Hepsiburada linki gönderin.")
    else:
        resp.message("Lütfen Hepsiburada'dan bir ürün linki gönderin. Örn: https://www.hepsiburada.com/...")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
