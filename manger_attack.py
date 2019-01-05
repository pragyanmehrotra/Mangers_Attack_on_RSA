#RSA module is imported for testing purposes only, You may remove this line before Usage
from rsa import decrypt,enc,rsa

import math

#decrypt function returns pow(c,d,n) or c**d % n where d is the private exponent
#obviously we couldn't directly decrypt the encrypted flag
#so we need an oracle to tell us wether after decrypting a certain integer it's > or < B

#TODO WRITE DECRYPT FUNCTION BEFORE RUNNING 

def oracle(c,B):
	'''
	oracle(c,B)
	B= 2**(8*(k-1))
	c -> ciphertext in integer to convert from plaintext to int do int(c.encode('hex'),16)
	returns true if (y**d)%n >= B else false
	us as the attacker don't have access to the private exponent so we need to make a decrypt function which communicates to the service	
	and let's us know the decrypted value.
	'''
	if decrypt(c) >= B:
		return True
	else:
		return False


#functions required for manger's attack
def f1(i):
	return (pow(2,i))
def f2(j,i):
	return ((n+B)/B + j)*f1(i-1)
def f3(ik,mmin,n):
	return (ik*n/mmin) + 1


##CHANGE n,e BEFORE RUNNING
n = rsa.n #plug-in the RSA modulus used for encryption
e = rsa.e #plug-in the RSA public exponent e usually 3,65537


k = int(math.ceil(math.log(n,256)))
B = pow(2,8*(k-1))
#print B
c = enc #plug-in your ciphertext as an integer if it's plaintext use int(16,ciphertext.encode('hex'))
print c
i=0
#query variable denotes the integer which needs to be passed to the oracle 
while True:
	query = (pow(f1(i),e,n)*c)%n
	if (oracle(query,B)):
		print i
		break
	i+=1
j=0
while True:
	query = (pow(f2(j,i),e,n)*c)%n
	if not (oracle(query,B)):
		print j
		break
	j+=1

mmin = n/f2(j,i) + 1
mmax = (n+B)/f2(j,i)

while mmax - mmin > 1:
	ftmp  = 2*B/(mmax-mmin)
	ik = ftmp*mmin/n
	f3k = f3(ik,mmin,n)
	query = (pow(f3k,e,n)*c)%n
	if (oracle(query,B)):
		mmin = ((ik*n+B)/f3k) + 1
	else:
		mmax = (ik*n +B)/f3k


#SUCCESS!!
m = mmin
print hex(m)[2:].strip('L').decode('hex')
#OR
m = mmax
print hex(m)[2:].strip('L').decode('hex')
	

	



