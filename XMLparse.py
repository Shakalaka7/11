import xmltodict

#Get el archivo de data XML 
stream = open('fileXML.xml','r')

#Analizar el formato XML a 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(type(e))