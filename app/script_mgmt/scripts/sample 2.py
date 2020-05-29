from xml.etree import ElementTree as ET

def main(file):
    return xml_mask(file)

def xml_mask(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for cus in root.findall('Customer'):
        cus.find('CustomerName').text = 'FAST FOOD'
        try:
            cus.find('PreferredName').text = 'JUNK FOOD'
        except:
            pass
    return tree
