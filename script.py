# -*- coding: utf8 -*-
import re
from pyparsing import *
import itertools


def textparse(a_name="sample.txt"):
    arquivo = open(a_name, "r")

    data = []
    for line in arquivo.readlines():
       if line != '\n':
           data.append('{' + line.strip() + '}')
    
    parsed_text = []
    for line in data:
        try:
            parsed_text.append(curlyparse(line))
        except:
            print "line error" #BUG BUG BUG

    return parsed_text
    
def bracketparse(p_text):
    nonchars = CharsNotIn("[]")
    defn = nestedExpr('[', ']', nonchars)
    lista = defn.parseString(p_text).asList()[0]
    options = []
    for item in lista:
        if isinstance(item, list):
            options.append(item[0])
    return options
    
def curlyparse(p_text):
    nonchars = CharsNotIn("{}")
    defn = nestedExpr('{', '}', nonchars)
    lista = defn.parseString(p_text).asList()[0]
    expressoes = []
    for item in lista:
        if isinstance(item, list):
            expressoes.append(bracketparse('[' + item[0] + ']'))
        else:
            expressoes.append([item])
    return expressoes
           
def generate(text):
    for x in itertools.product(*text):
        print " ".join(x)

parsed_text = textparse("sample.txt")
for i in parsed_text:
    generate(i)
