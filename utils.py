def format_scorecard(product_data):
    name = product_data.get("name", "Ürün Bilgisi Yok")
    price = product_data.get("price", "Fiyat Bilgisi Yok")
    scores = product_data.get("scores", {})

    lines = [f"📌 *{name}*", f"💸 *Fiyat:* {price}", "", "### Skorlar (100 üzerinden)"]

    for label, score_info in scores.items():
        value = score_info.get("value", "-")
        note = score_info.get("note", "")
        emoji = {
            "Satisfaction": "✅",
            "Risk": "🧯",
            "Feel": "💠",
            "Expert Test": "⚙️"
        }.get(label, "•")
        lines.append(f"{emoji} *{label}:* {value}\n_{note}_")

    return "\n".join(lines)
