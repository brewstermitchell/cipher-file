#!/usr/bin/env python
####
# Cypher-file: contains functions to encypher and decypher files into base64. (weak cipher)
# written by Brewster Mitchell
#   April 11, 2016
# See LICENSE.md for license terms.
#####

import sys
import base64


in_f = sys.argv[1]
out_f = sys.argv[2]

print(type(in_f))
print(type(out_f))

def encrypt (in_file, out_file):
  with open(in_file) as f:
    encoded = base64.b64encode(f.read())
    print(encoded)
    with open(out_file, 'w') as w:
      w.write(encoded)
      
def decrypt (out_file, in_file):
  with open(out_file) as f:
    decoded = base64.b64decode(f.read())
    print(decoded)
    
# encrypt(in_f, out_f)
# decrypt(out_f, in_f)