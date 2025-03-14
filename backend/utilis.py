import validators

def is_valid_url(url):
    return validators.url(url)
