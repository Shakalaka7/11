import json

jsonstr = """{"people":[{"Id":"1","FirstName":"Fernando","LastName":"Chacon",
    "Email":"francofer7775@gmail.com"},{"Id":"2","FirstName":"Vinitri","LastName":"Leal",
    "Email":"vinitrileal@yahoo.com"},{"Id":"3","FirstName":"Paty","LastName":"Acevedo",
    "Email":"paty.acevedo@yahoo.com"}]}"""

jsonobj = json.loads(jsonstr)

print(jsonobj['people'][1])
print("""********************************************************************************""")
jsonobj = json.load(open('fileJson.json'))

print(jsonobj['people'])