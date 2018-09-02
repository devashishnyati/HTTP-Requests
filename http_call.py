import requests

for i in range(3):
    r = requests.get('https://webhook.site/9713cf49-d43c-477f-9a22-ccd1a5458e81')
    print('Response ID: {} \tResponse Time: {}'.format(r.headers['X-Request-Id'], r.headers['date']))