'''Python program for encoding and decoding using Base64'''

import base64

data = "Python is a programming language"

data_bytes = data.encode('ascii')

base64_bytes = base64.b64encode(data_bytes)

print("Encoded Data: ", base64_bytes)

