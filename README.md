# Mangers_Attack_on_RSA
Implemented in python 2.7

performs the basic implementation of manger's attack as shown in https://research.kudelskisecurity.com/2018/04/05/breaking-rsa-oaep-with-mangers-attack/
Well the code was inspired by a challenge while I was doing a CTF but unfortunately the challenge didn't require a manger's attack on it but this paper or algorithm of narrowing down the possibilities to a single message in O(logN) time caught my interest.
I felt like coding it so here it is,

# Usage

python manger_attack.py

before running the code manger_attack.py
Note :- rsa.py is not needed it was just implemented to test the functioning of the attack.
Therefore you need to change the value of n and e in the script to your custom input of rsa modulus and rsa public exponent
Moreover if you understand what all conditions must be met before performing a manger's attack you'd need an oracle function which returns true if (c^d)%n >= B else false now obviously we won't have access to the private exponent 'd' but we might have access to the decryption which obviously doesn't return the decrypted version of the ciphertext we want decrypted thus feel free to customize the function oracle as you may like
