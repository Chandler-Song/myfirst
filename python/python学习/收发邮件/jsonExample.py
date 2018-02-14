#json
stringOfJsonData = '{"isCat": true, "miceCaught": 0, "name": "Zophie", "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
#AttributeError: 'str' object has no attribute 'decode'
#So it's JSON, encoded as UTF-8, and Python is considering it a byte stream, not a simple string. In order to parse this, you need to convert it into a string first.
#要求内部为"" 外部为'
#loads()
pythonValue = {"isCat" : True, "miceCaught" : 0, "name" : "Zophie", "felineIQ" : None}
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
