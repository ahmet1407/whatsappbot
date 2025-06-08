import re

def clean_url(text):
    """Yorum içinden düzgün bir Hepsiburada linki bulur."""
    url_pattern = r"(https?://[^\s]+)"
    match = re.search(url_pattern, text)
    return match.group(0) if match else None
