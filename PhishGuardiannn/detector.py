# detector.py

from utils.url_features import extract_features

def detect_url(url):
    features = extract_features(url)
    score = 0

    # Feature-based detection logic (adjusted for better detection)
    if features["has_ip"]:  # If URL has IP address instead of domain
        score += 1
    if features["has_at_symbol"]:  # If URL contains "@" symbol
        score += 1
    if features["has_redirect"]:  # If URL has "redirect" or similar keywords
        score += 1
    if features["url_length"] > 75:  # Long URL length is often suspicious
        score += 1
    if features["has_http"]:  # Check if HTTP/HTTPS is present
        score += 1
    if features["has_suspicious_keywords"]:  # Common phishing keywords
        score += 1

    # If score >= 3, it is likely phishing
    if score >= 3:
        return "⚠️ Phishing URL Detected!"
    else:
        return "✅ URL Seems Safe."
