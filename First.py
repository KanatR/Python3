import requests

address = '4Jb9EzcUd6k1gC7GSH2iu6H7UcL2ez3NgvAF8n6a1QDs'

url = 'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'

headers = {

    "accept": "application/json",
    "X-API-Key": "SWnpmagdLrYt67aFhsaBRRzoubD59cdQkydkZLeljvVREBpWGmpLktfRLZXcvudp"

}

response = requests.get(url, headers=headers)

print(response.text)