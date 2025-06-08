def detect_platform(url):
    if "hepsiburada.com" in url:
        return "hepsiburada"
    elif "trendyol.com" in url:
        return "trendyol"
    elif "amazon.com.tr" in url:
        return "amazon"
    else:
        return "unknown"
