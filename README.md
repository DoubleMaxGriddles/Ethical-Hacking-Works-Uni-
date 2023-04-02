# Ethical-Hacking-Works-Uni-
Projects and Works for Ethical Hacking.

ransomeware.py
--------------------------------------------------------------------------------------------------------------------------------------------------
Create a simple ransomware, which is a Python program. 
The assumption is the following: 
1) An attacker breaks
into a victim’s machine, which can run GPG; 
2) the attacker put their public key in the victim’s machine; 
3) the victim has a file named important.txt in his root directory (You can write anything in important.txt.)

The ransomware should perform the following:
1) It asks the attacker to type a key (for symmetric encryption) and saves it to a file named key.txt.
2) Then it encrypts the file important.txt using the key that the attacker selected in step 1); 
the format of the resulting ciphertext should be ASCII so that it has a file extension .asc at the end. - We call this
ciphertext encrypted_message.asc.
3) The file key.txt will be encrypted using the attacker’s public key;
the format of the resulting ciphertext should be ASCII so that it has a file extension .asc at the end as ciphertext encrypted_key.asc.
4) The file key.txt will be deleted.
5) The file important.txt will be deleted
6) It will finally display a message for ransom “Your file important.txt is encrypted. To decrypt it, you need to pay me $1,000 and send encrypted_key.asc to me.” 

On Ubuntu, generate the key using:

gpg --gen-key 

use your password (mine is 'max')

then export it using:

gpg --armor --export (email) > pubkey.gpg.asc

then run the ransomeware
--------------------------------------------------------------------------------------------------------------------------------------------------

backdoortrojan.py
A simple trojan virus desgined to access the backdoor.
