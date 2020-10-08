import xml.etree.cElementTree as ET
from lxml import etree

#tree = ET.parse('configuration.xml')
tree = ET.ElementTree(file='configuration.xml')
root = tree.getroot()

def setType(x):
    mode = root.find('type')
    mode.text=x
    tree.write('configuration.xml')


def getType():
    mode = root.find('type')
    print (mode.text)
    return mode.text


def set_Min_Max(x,y):
    mode = root.find('modifer/a')
    mode.text=str(x)
    mode = root.find('modifer/b')
    mode.text=str(y)
    tree.write('configuration.xml')

def set_Val(NameVale,val):
    mode = root.find(NameVale)
    mode.text=str(val)
    tree.write('configuration.xml')
