#!/usr/bin/env python3
"""import add from the previous file and annotate it correctly
"""
add = __import__('0-add').add

print(add(1.0, 2.0) == 1.0 + 2.0)
print(add.__annotations__ == {'a': float, 'b': float, 'return': float})