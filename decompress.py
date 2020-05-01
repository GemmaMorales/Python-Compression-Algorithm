# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):
    decompressed_content = compressed_content
    for key in symbols:
        replaced = decompressed_content.replace(symbols[key], key)
        decompressed_content = replaced 
    print(decompressed_content)
    return decompressed_content
    