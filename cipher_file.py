#!/usr/bin/env python
####
# Cypher-file: contains functions to encipher and decipher files into base64. (weak cipher)
# written by Brewster Mitchell
#   April 11, 2016
# See LICENSE.md for license terms.
#####

import sys
import base64


in_f = sys.argv[1]
out_f = sys.argv[2]


def encrypt (in_file, out_file):
  with open(in_file, 'rb') as f:
    encoded = base64.b64encode(f.read())
    with open(out_file, 'wb') as w:
      w.write(encoded)
      
def decrypt (out_file, in_file):
  with open(out_file, 'rb') as f:
    decoded = base64.b64decode(f.read())
    with open(in_file, 'wb') as w:
      w.write(decoded)
      
    
encrypt(in_f, out_f)
decrypt(out_f, 'result.xml')