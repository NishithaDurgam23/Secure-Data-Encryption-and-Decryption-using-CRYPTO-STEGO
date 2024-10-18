from flask import Flask, render_template, request
import os
import base_enc
import rsa_enc
import stego_enc
import stego_dec
import rsa_dec
import base_dec

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Encryption')
def encrypt():
    return render_template('Encryption.html')

@app.route('/Decryption')
def decrypt():
    return render_template('Decryption.html')

@app.route('/Encryption', methods=['POST'])
def getdata_enc():
    source_name = request.form['source_name']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    cover_name = request.form['cover_name']
    new_img_name = request.form['new_name']

    base_enc.base_enc(source_name)
    rsa_enc.call_rsa('s.txt', p, q)
    cover_path = os.path.join(os.path.dirname(__file__), 'static', 'coverimages', cover_name)
    stego_enc.encode(cover_path, new_img_name)

    return render_template('thank.html')

@app.route('/Decryption', methods=['POST'])
def getdata_dec():
    cover_name = request.form['cover_name']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    new_cover_name = request.form['new_cover_name']

    stego_dec.decode(cover_name)
    rsa_dec.rsa_dec(p,q)
    base_dec.base_dec(new_cover_name)

    return render_template('thank.html')

if __name__ == "__main__":
    app.run(debug=True)
