# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'


DELAYS = {
    'ACCOUNT': [15, 45],  # delay between connections to accounts (the more accounts, the longer the delay)
    'REPEAT': [300, 600]
}

PROXY_TYPES = {
    "TG": "http",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
    "REQUESTS": "http"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
