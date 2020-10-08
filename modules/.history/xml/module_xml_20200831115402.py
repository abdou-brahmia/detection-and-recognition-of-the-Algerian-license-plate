import xml.etree.cElementTree as ET
from lxml import etree

#tree = ET.parse('configuration.xml')
tree = ET.ElementTree(file='configuration.xml')
root = tree.getroot()

#print (root.tag )#parameters
#print(root[0].tag )#'name'
#print(root[0].text)#'test'
#print(root[1].tag )#'version'
#print(root[1].text )#'1.0'
#root[1].text="3.0"
#print(root[1].text )#'2.0'
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
    mode = root.find('modifer/b')
    mode.text=str(y)
    tree.write('configuration.xml')
