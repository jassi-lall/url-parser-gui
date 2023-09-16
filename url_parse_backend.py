from urllib.parse import urlparse, parse_qs
import pandas as pd

def pretty_parse(url):
    parsed_url = urlparse(url)
    d = pd.Series(
        data=[parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.fragment],
        index=['scheme', 'netloc', 'path', 'fragment'])
    
    q = parse_qs(parsed_url.query) # dict of url parameters
    
    # Reformat so url parameters with a unique value are a value instead of a list with one element
    for key in q:
        if len(q[key]) == 1:
            q[key] = q[key][0]
    
    q = pd.Series(q)

    return d.to_string(header=False, dtype=False) + "\n\nquery\n" + q.to_string(header=False, dtype=False)