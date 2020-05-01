 # !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "implementation":   "🤯",
    "practicality"  :   '🤩',
    "better"        :   '😅',
    "than"          :   '😘',
    "Although"      :   "🥺",
}

def compress(content):
    compressed_content = content
    for key in symbols:
        replaced = compressed_content.replace(key, symbols[key])
        compressed_content = replaced
    #print(compressed_content)
    return compressed_content