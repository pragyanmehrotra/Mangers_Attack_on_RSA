import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

flag = "flag{f1nd_m3_1f_you_c4n_th1s_s0m3_s3cr3t_m3ss4g3}"

def encrypt(m):
	return pow(m,rsa.e,rsa.n)
def decrypt(c):
	if (check_num(c)):
		return pow(c,rsa.d,rsa.n)
def check_num(c):
	if c == int(enc):
		return False
	else:
		return True

rsa = RSA.generate(2048)
enc = encrypt(int(flag.encode('hex'),16))
