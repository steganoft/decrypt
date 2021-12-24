#!/usr/bin/python

from cryptosteganography import CryptoSteganography

IMAGE_LOCATION = 'nft.png'
NFT_PASSWORD = 'ExamplePassw0rd'

stegopass = CryptoSteganography(NFT_PASSWORD)
secret = stegopass.retrieve(IMAGE_LOCATION)

print(f'Secret Message: {secret}')
