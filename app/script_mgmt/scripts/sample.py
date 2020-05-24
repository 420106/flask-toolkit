from xml.etree import ElementTree as ET

def main(file):
    return mask(file)

def mask(file):
    tree = ET.parse(file)
    root = tree.getroot()
    root.find('TestField').text = 'Masked'
    return tree
