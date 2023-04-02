import base64
import binascii
from Crypto import Random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


def toBase64(string):
    return base64.b64encode(string)


# function to generate public and private key pairs

def generateKeys():
    length = 1024   # since we need the lenght of the keys to be 1024 bits.

    priKey = DSA.generate(length, Random.new().read)
    pubKey = priKey.publickey()
    return priKey, pubKey


def generateFormattedKeys(pri, pub):
    private = pri.exportKey().decode()
    public = pub.exportKey().decode()
    return private, public


N = int(input("Enter the number of N: "))

arr = []

for i in range(N):
    pri, pub = generateKeys()
    arr.append((pri, pub))


print("\nThe private\\public key pairs generated are:\n")
for i in arr:
    p = binascii.hexlify(i[0].exportKey())
    pb = binascii.hexlify(i[1].exportKey())
    print(p, pb)


f = open("scriptPubKey.txt", "w")
f.write(str(arr))
f.close
print("Message Written Successfully")

# this method will be used to generate signatures using the private keys generated.


def generateSignatures(key):
    # Sign a message
    message = b"CSCI301 Contemporary topic in Security"
    hash_obj = SHA256.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature


M = int(input("Enter the value of M. It should be less than or equal to N: "))

if(M > N):
    print("The value of M is greater than N. The program is terminated.")

else:
    # read the public and private keys from the txt file.
    f = open("scriptPubKey.txt", "r")
    array = f.read()
    f.close
    print("Read Successfully.")
    # convert it back into list format.
    # arr = list(arr)
    print("\n The values are:\n")
    print(array)
    sigArr = []

    for i in range(0, M):
        print("\nThis is the value of Private key:\n")
        print(binascii.hexlify(arr[i][0].exportKey()))
        sign = generateSignatures(arr[i][0])
        # print(arr[i][i])
        sigArr.append(sign)
    f = open("scriptSig.txt", "w")
    f.write(str(sigArr))
    f.close
    print("\nSignatuers Written in scriptSig.txt successfully.\n")
    print("The values in scriptSig.txt is: \n")
    f = open("scriptSig.txt", "r")
    print(binascii.hexlify(bytes(f.read().encode())))
    f.close()
