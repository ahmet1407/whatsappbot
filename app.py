from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scorecard_logic import analyze_product_from_hepsiburada
import re

app = Flask(__name__)

@app.route("/message", methods=['POST'])
def message():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    
    hepsiburada_url_pattern = r"(https?://(?:www\.)?hepsiburada\.com\S+)"
    match = re.search(hepsiburada_url_pattern, incoming_msg)

    if match:
        url = match.group(1)
        result = analyze_product_from_hepsiburada(url)

        msg = f"📄 *{result['name']}*\n💰 {result['price']}\n\n"
        for key, val in result["scores"].items():
            msg += f"*{key}:* {val['value']}\n{val['note']}\n\n"

        resp.message(msg.strip())
    else:
        resp.message("🔗 Lütfen geçerli bir Hepsiburada ürün linki gönderin.")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
