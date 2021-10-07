import pyDH
import requests

d2 = pyDH.DiffieHellman() #We generate the diffie helman key from the client
d2_pubkey = d2.gen_public_key()
#d2_sharedkey = d2.gen_shared_key(d1_pubkey)

response = requests.get(f'http://127.0.0.1:5000/getpubkey/{d2_pubkey}')
d2_sharedkey = d2.gen_shared_key(int(response.text))
print(f'la llave sincronizada es: {d2_sharedkey}')

#https://github.com/amiralis/pyDH