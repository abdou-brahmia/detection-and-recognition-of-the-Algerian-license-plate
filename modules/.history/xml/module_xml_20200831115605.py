import xml.etree.cElementTree as ET
from lxml import etree

tree = ET.ElementTree(file='configuration.xml')
root = tree.getroot()


def get_Val(NameVale):
    mode = root.find(NameVale)
    #print (mode.text)
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
