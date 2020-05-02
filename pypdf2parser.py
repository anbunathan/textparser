# importing required modules
import PyPDF2
import os
import re
from collections import OrderedDict
# creating a pdf file object
pdfFileObj = open('documents/LearningParseStructures.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
number_of_pages=pdfReader.numPages
print(pdfReader.numPages)
text = ""
# creating a page object
for page_number in range(number_of_pages):
    print('page number = ', page_number)
    pageObj = pdfReader.getPage(page_number)
    text += pageObj.extractText()
    # extracting text from page
    # print(pageObj.extractText())
text = text.encode('ascii','ignore').lower() #Lowercasing each word
# text = str(text)
# text = re.sub('\d+', 'NUMBER', text)
# text = re.sub('NUMBER,NUMBER', '', text)
# text = re.sub('NUMBER.NUMBER', '', text)
# text = re.sub('NUMBER.', '', text)
# text = re.sub('NUMBER', '', text)
# text = re.sub(r'\t+', '', text)
# text = re.sub(r'^$\n+', '', text, flags=re.MULTILINE)
# text = re.sub("[!@#$+%*:()'-]", '', text)
# text = os.linesep.join([s for s in text.splitlines() if s])
# text = "\n".join(list(OrderedDict.fromkeys(text.split("\n"))))
# text = re.sub('(?m)^.{0,100}\n','',text)
# paragraphs = text.split('\n')
# for paragraph in paragraphs:
#     print(paragraph)
print("text =", text)
# closing the pdf file object
pdfFileObj.close()
