import xml.etree.cElementTree as ET
from lxml import etree

tree = ET.ElementTree(file='modules/xml/configuration.xml')
root = tree.getroot()


def get_Val(NameVale):
    mode = root.find(NameVale)

    return int(mode.text)

def set_Val(NameVale,val):
    mode = root.find(NameVale)
    mode.text=str(val)
    tree.write('modules/xml/configuration.xml')
