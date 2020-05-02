# some python file
import textract

#text = textract.process("documents/all_val.txt")
text = textract.process("documents/LearningParseStructures.docx")
paragraphs = text.splitlines()
paragraphs1 = text.decode('utf_8').split('\n')
print(text)
print(paragraphs)
print(paragraphs1)

# text = textract.process("documents/Bibliography.docx")
# print(text)
#
# text = textract.process("documents/IOT.pptx")
# print(text)

# text = textract.process("documents/bank.csv", errors='ignore', engine='python', encoding = "ascii")
# print(text)

# text = textract.process("documents/file_example_XLS_5000.xls", errors='ignore', engine='python', encoding = "ascii")
# print(text)
#
# text = textract.process("documents/file_example_XLSX_5000.xlsx", errors='ignore', engine='python', encoding = "ascii")
# print(text)


