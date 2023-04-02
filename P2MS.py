import base64
import binascii
from inspect import stack
from Crypto import Random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


def generateKeys():
    length = 1024   # since we need the lenght of the keys to be 1024 bits.

    priKey = DSA.generate(length, Random.new().read)
    pubKey = priKey.publickey()
    return priKey, pubKey


N = int(input("Enter the number of N: "))

stackPubKey = []
stackPriKey = []

for i in range(N):
    pri, pub = generateKeys()
    stackPriKey.append(pri)     # put the primary keys in a separate stack
    stackPubKey.append(pub)     # put the public keys in a separate stack.

# the message that needs to be signed.
message = b"CSCI301 Contemporary topic in Security"


def generateSignatures(key):
    # Sign a message

    hash_obj = SHA256.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature


def checkMultiSig(signature, pubkey):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(pubkey, 'fips-186-3')
    try:
        verifier.verify(hash_obj, signature)
        print("The message is authentic.")
    except ValueError:
        print("The message is not authentic.")


M = int(input("Enter the value of M. It should be less than or equal to N: "))

signatureStack = []     # here is the signature stack.


if(M > N):
    print("The value of M is greater than N. The program is terminated.")
else:
    for i in range(M):
        # now we generate the digital signatures using the private keys.
        sign = generateSignatures(stackPriKey[i])
        # now we put the generated signatures in the stacks in the same order as the public keys.
        signatureStack.append(sign)
    # now we authenticate the script.
    for i in range(M):
        checkMultiSig(signatureStack[i], stackPubKey[i])
