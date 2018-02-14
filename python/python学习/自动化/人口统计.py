import openpyxl, pprint

print("Opening workbook...")

wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")

countyData = {}

#TODO:Fill in countrydata with each country's population and tracts.
print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value
#填充countyADta
    countyData.setdefault(state ,{})
    countyData[state].setdefault(county, {"tract" : 0, "pop" : 0})
    countyData[state][county]["tract"] += 1
    countyData[state][county]["pop"] += int(pop)
#TODO:Open a new text file and write the contents of countyData to it
print("Writing results...")
resultFile = open("census2010.py", "w")
resultFile.write("allData = " + pprint.pformat(countyData))
resultFile.close()
print("Done.")
#查看文件 import census2012.py census2012.allData["AK"]["Anchorage"]["pop]