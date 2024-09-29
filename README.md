# rfc5990bis-examples

Some examples of envelopedData and authEnvelopedData objects using RSA-KEM from RFC5990bis using KEMRecipientInfo as specified in RFC 9629

## Example files
1. __rfc5990bis-1-def.p7m__ -- Use defaults for RSA-KEM: aes128-CBC, kdf3/sha-256/aes128-wrap. Recipientidentifier is default CHOICE issuerAndSerialNumber.
2. __rfc5990bis-2-ski.p7m__ -- As for (1) but use subjectKeyIdentifier instead of issuerAndSerialNumber.
3. __rfc5990bis-3-hkdf.p7m__ -- As for (2) but use HKDF instead of default KDF3.
4. __rfc5990bis-4-gcm.p7m__ -- As for (2) but use AES-128-GCM from RFC 5116 in an authEnvelopedData object.
5. __rfc5990bis-5-chachapoly.p7m__ -- As for (4) but use AEAD_CHACHA20_POLY1305 authenticated encryption algorithm from RFC 8439.
6. __rfc5990bis-6-ukm.p7m__ -- As for (2) but add user keying material (ukm).

## Key and certificate used

+ __rfc5990bis-bob.p8.pem__ -- Bob's 3072-bit RSA private key from RFC5990bis, no password.
+ __rfc5990bis-bob.cer__ -- A made-up self-signed X.509 certificate using Bob's public key and subjectKeyIdentifier from RFC5990bis.


## Subfolders

+ __asn1dumps__ -- ASN.1 structures created using DUMPASN1

+ __pemfiles__ -- Textual encodings of binary .p7m files

+ __pycode__ -- Python code to create the examples.

These example files were created using v23.0 of the [CryptoSys PKI Toolkit](https://www.cryptosys.net/pki).

Note that the Python code uses random input each time it is used, so the output files will have different values each time but the same ASN.1 structure.

David Ireland  
CryptoSys, Australia  
<https://www.cryptosys.net/contact/>
