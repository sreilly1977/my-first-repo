#!/usr/bin/python3

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
 print(response.headers.get('X-Request-Id'))

# Got stuck looking for urllib. I'm running on my home Linux workstation and it works this way.
