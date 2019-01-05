# Mangers_Attack_on_RSA
Implemented in python 2.7

Performs the basic implementation of Manger's attack as shown in https://research.kudelskisecurity.com/2018/04/05/breaking-rsa-oaep-with-mangers-attack/

### Motivation
The code was inspired by a challenge while I was doing a CTF. Unfortunately, the challenge actually didn't require a Manger's attack, but this algorithm of narrowing down the possibilities to a single message in logN queries caught my interest.

## Usage

```python manger_attack.py```

*Note* :- rsa.py is not needed. It was implemented just to test the functionality of the attack.
You need to change the value of n and e in the script to your custom input of RSA modulus and RSA public exponent. Also, you may need to customize the ```oracle``` function such that it returns true if (query<sup>d</sup>%n) >= B, else false. Obviously, we won't have access to the private exponent 'd', but we might have access to the decryption service (which excludes the given ciphertext).
