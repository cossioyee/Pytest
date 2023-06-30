def lambda_handler(event, context):
    response = event['Records'][0]['cf']['response']
    headers = response['headers']

    security_headers = {
        'strict-transport-security': [{
            'key': 'Strict-Transport-Security',
            'value': 'max-age=31536000; includeSubDomains; preload'
        }],
        'x-content-type-options': [{
            'key': 'X-Content-Type-Options',
            'value': 'nosniff'
        }],
        'x-frame-options': [{
            'key': 'X-Frame-Options',
            'value': 'DENY'
        }],
        'x-xss-protection': [{
            'key': 'X-XSS-Protection',
            'value': '1; mode=block'
        }],
        'referrer-policy': [{
            'key': 'Referrer-Policy',
            'value': 'same-origin'
        }],
        'cache-control': [{
            'key': 'Cache-Control',
            'value': 'public, max-age=86400'
        }]
    }

    headers.update(security_headers)

    return response