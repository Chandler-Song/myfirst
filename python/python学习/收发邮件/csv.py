#csv文件操作实列
import csv
exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
#for 从Reader对象读取数据
import csv
for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + ' ' + str(row))
#Writer对象
import csv
outputFile = open("output.csv", "w", newline = "")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(["sapm", "eggs", "bacon", "ham"])
outputWriter.writerow(["hello, world", "eggs", "bacon", "ham"])
outputFile.close()
#delimiter and lineterminator关键字参数
import csv
outputFile = open("output.csv", "w", newline = "")
outputWriter = csv.writer(outputFile, delimiter = '\t', lineterminator = "\n\n")
outputWriter.writerow(["sapm", "eggs", "bacon", "ham"])
outputWriter.writerow(["hello, world", "eggs", "bacon", "ham"])
outputFile.close()
