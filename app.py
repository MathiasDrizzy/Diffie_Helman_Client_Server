from flask import Flask
import pyDH
import logging

app = Flask(__name__)

#Desactivate log messages
log = logging.getLogger('werkzeug')
log.disabled = True


@app.route('/getpubkey/<int:d2_pubkey>')
def key(d2_pubkey):
    d1 = pyDH.DiffieHellman()
    d1_pubkey = d1.gen_public_key()
    d1_sharedkey = d1.gen_shared_key(d2_pubkey)
    print(f'la llave sincronizada es: {d1_sharedkey}')
    return str(d1_pubkey)




