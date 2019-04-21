import xml.etree.ElementTree as ET
import random

import logging 

bestFitTree = ET.parse('xml/unicode.xml')
bestFitRoot = bestFitTree.getroot()

unicodeTree = ET.parse('xml/expandedUnicode.xml')
unicodeRoot = unicodeTree.getroot()

def getExpandedUnicode():
    unicodeList = []
    for unicode in unicodeRoot.findall('Mapping'):
        string = '\\U' + unicode.find('Unicode').text
            
        unicodeText = string.encode('utf-8')
        decodedValue = unicodeText.decode('unicode_escape')
        unicodeList.append(decodedValue)

    if len(unicodeList) > 0:
        randIndex = random.randint(0, len(unicodeList) - 1)
        #print(unicodeList[randIndex])
        return unicodeList[randIndex]
    else:
        #print('\\u0263'.encode('utf-8').decode('unicode_escape'))
        return '\\u0263'.encode('utf-8').decode('unicode_escape')

def getBestFit(character):
    bestfitList = []
    charValue= ord(character)
    #print(charValue)
    for unicode in bestFitRoot.findall('Mapping'):
        asciiValue = int(unicode.find('Ascii').text[2:], 16)
        if charValue == asciiValue:
            #print(unicode.find('Unicode').text)
            string = '\\u' + unicode.find('Unicode').text
            
            unicodeText = string.encode('utf-8')
            #print(string)
            #print(unicodeText)
            #print(unicodeText.decode('unicode_escape'))
            #print(unicode.find('Name').text)
            decodedValue = unicodeText.decode('unicode_escape')
            bestfitList.append(decodedValue)

    if len(bestfitList) > 0:
        randIndex = random.randint(0, len(bestfitList) - 1)
        #print(bestfitList[randIndex])
        return bestfitList[randIndex]
    else:
        #print('\\u0263'.encode('utf-8').decode('unicode_escape'))
        return character
