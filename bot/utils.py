import re

def is_valid_url(url):
    # Regular expression for a basic URL validation
    url_pattern = re.compile(
        r'^(https?://)?'  # Optional http or https
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain (TLD)
        r'(/[a-zA-Z0-9_.-]*)*'  # Path
        r'(\?[a-zA-Z0-9&=_.-]*)?'  # Query parameters
        r'(#\w*)?$'  # Fragment identifier
    )
    
    return bool(re.match(url_pattern, url))