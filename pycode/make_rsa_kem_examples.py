# make_rsa_kem_examples.py

"""
Requires (1) CryptoSys PKI Pro v23.0 to be installed on your system
-- available at https://www.cryptosys.net/pki/
and (2) the Python interface to CryptoSys PKI
-- available at https://pypi.org/project/cryptosyspki/
pip install cryptosyspki

NOTE Each run will produce different output files.
"""

from cryptosyspki import *  # @UnusedWildImport

print("\nTESTING CMS ENV DATA USING RSA-KEM...")
certfile = "../certs-and-keys/rfc5990bis-bob.crt"  # A made-up self-signed certificate using Bob's public key from RFC5990bis
keyfile = "../certs-and-keys/rfc5990bis-bob.p8.pem"  # Bob's 3072-bit RSA key from RFC5990bis, no password
inputdata = "Hello, world!"

# 1. Use defaults for RSA-KEM: aes128-CBC, kdf3/sha-128/aes128-wrap. Recipientidentifier is default CHOICE issuerAndSerialNumber
edfile = "rfc5990bis-1-def.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM)
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata

# 2. As for (1) but use subjectKeyIdentifier instead of issuerAndSerialNumber
edfile = "rfc5990bis-2-ski.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM, opts=Cms.EnvDataOpts.USE_SKI)
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata

# 3. As for (2) but use HKDF instead of default KDF3
edfile = "rfc5990bis-3-hkdf.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM, opts=Cms.EnvDataOpts.USE_SKI, kdfalg=Kdf.KdfAlg.HKDF)
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata

# 4. As for (2) but use AES-128-GCM from RFC 5116 in an authEnvelopedData object
edfile = "rfc5990bis-4-gcm.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM, opts=Cms.EnvDataOpts.USE_SKI, cipheralg=Cms.ContentEncrAlg.AES_128_GCM)
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata

# 5. As for (4) but use AEAD_CHACHA20_POLY1305 authenticated encryption algorithm from RFC 8439
edfile = "rfc5990bis-5-chachapoly.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM, opts=Cms.EnvDataOpts.USE_SKI,  cipheralg=Cms.ContentEncrAlg.CHACHA20_POLY1305)
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata

# 6. As for (2) but add user keying material (ukm)
edfile = "rfc5990bis-6-ukm.p7m"  # Output file
r = Cms.make_envdata_from_string(edfile, inputdata, certfile, keyencralg=Cms.KeyEncrAlg.RSA_KEM, opts=Cms.EnvDataOpts.USE_SKI, keyString='some user key info')
print(f"Created file {edfile}")
# Read enveloped data
prikeystr = Rsa.read_private_key(keyfile)
s = Cms.read_envdata_to_string(edfile, prikeystr)
print(f"Plaintext is '{s}'")
assert s == inputdata
