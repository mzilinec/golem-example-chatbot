from urllib.parse import urlparse

import os

redis_url = os.environ.get('REDIS_URL', "redis://localhost:6379/0")

if redis_url:
    redis_url_parsed = urlparse(redis_url)
    REDIS_CONF = {
        'HOST': redis_url_parsed.hostname,
        'PORT': redis_url_parsed.port,
        'PASSWORD': redis_url_parsed.password
    }
else:
    raise Exception('Redis URL not set')

GOLEM_CONFIG = {
    "BOTS": {
        "keepbot/bots/flows.yaml"
    },
    "REDIS_URL": redis_url,
    "REDIS": REDIS_CONF,
    "WIT_TOKEN": "WWUACLPCWMSLVOWLEJG6YO3V5J42DQAZ",
    'FB_PAGE_TOKEN': os.environ.get('FB_PAGE_TOKEN'),  # used to link facebook page
    'WEBHOOK_SECRET_URL': os.environ.get('WEBHOOK_SECRET_URL'),  # used to hide chatbot url from 3rd party
    'WEBHOOK_VERIFY_TOKEN': os.environ.get('WEBHOOK_VERIFY_TOKEN'),  # used to verify facebook webhooks
    'DEPLOY_URL': os.environ.get('DEPLOY_URL'),
    'MSG_LIMIT_SECONDS': 20,
}
