# utils/url_features.py

import re
from urllib.parse import urlparse

def extract_features(url):
    features = {
        "has_ip": False,
        "has_at_symbol": False,
        "has_redirect": False,
        "url_length": len(url),
        "has_http": False,
        "has_suspicious_keywords": False
    }
    
    # Check if the URL contains an IP address (suspicious)
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        features["has_ip"] = True
    
    # Check for @ symbol in URL (phishing red flag)
    if "@" in url:
        features["has_at_symbol"] = True
    
    # Check for redirect words like "redirect", "click", "secure", etc.
    if any(keyword in url for keyword in ["redirect", "login", "secure", "account", "update"]):
        features["has_redirect"] = True
    
    # Check if URL has HTTP (not secure)
    if "http://" in url:
        features["has_http"] = True
    
    # Look for suspicious keywords in the URL
    if any(keyword in url for keyword in ["login", "secure", "account", "update", "free", "claim", "bank", "password"]):
        features["has_suspicious_keywords"] = True

    return features
