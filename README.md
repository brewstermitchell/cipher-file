# Cipher-File

Python 3.x module containing functions to encipher and decipher files using a key (passphrase).<br />
Intended for either importing or calling directly with the specified parameters.

## Usage:


##### Dependencies:
 
Python 3.x<br />
PyCrypto

##### Parameters:

*[1]*  e / d = select **e**ncipher or **d**ecipher

*[2]*  file in = the file to be en/deciphered.

*[3]*  file out = the filename of the en/deciphered result

*[4]*  key = string key to create cipher (or to generate same cipher for decipher). Can be any length.
 
 
##### CLI

cipher-file.py [e/d] [file in] [file out] [key]<br />
ex:<br />
```
 python3 cipher-file.py e plaintext.txt enctext.txt pa$$w0rd
```

## License:

  See LICENSE.md