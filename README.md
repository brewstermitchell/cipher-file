# Cipher-File

Python module containing functions to encipher and decipher files using a key (passphrase).
Intended for either importing or calling directly with the specified parameters.

## Usage:

###### Parameters:

 [1] e / d = select __e__ncipher or __d__ecipher
 
 [2] file in = the file to be en/deciphered.
 
 [3] file out = the filename of the en/deciphered result
 
 [4] key = string key to create cipher (or to generate same cipher for decipher). Can be any length.
 
 
###### CLI

 cipher-file.py [e/d] [file in] [file out] [key]
 
 ex: 'python3 cipher-file.py e plaintext.txt enctext.txt pa$$w0rd'

## License:

  See LICENSE.md