import re
import numpy as np
from urllib.parse import urlparse

def extract_features(url):
    parsed_url = urlparse(url)
    
    # Basic URL features
    length_of_url = len(url)
    length_of_hostname = len(parsed_url.netloc)
    num_digits = sum(c.isdigit() for c in url)
    num_special_chars = len(re.findall(r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]", url))
    num_subdomains = parsed_url.netloc.count('.')

    return [length_of_url, length_of_hostname, num_digits, num_special_chars, num_subdomains]
