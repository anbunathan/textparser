import os
import re
from collections import OrderedDict
from tika import parser

raw = parser.from_file("documents/LearningParseStructures.pdf")
raw = raw["content"]
raw = str(raw)
safe_text = raw.encode('utf-8', errors='ignore')
safe_text = str(safe_text).replace("\n", "").replace("\\", "$$$$")
safe_text = safe_text.replace('$$$$n', '').replace("b\'", '')
# print('--- safe text ---' )
# print( safe_text )
text = safe_text

text = re.sub('\d+', 'NUMBER', text)
text = re.sub('NUMBER,NUMBER', '', text)
text = re.sub('NUMBER.NUMBER', '', text)
text = re.sub('NUMBER.', '', text)
text = re.sub('NUMBER', '', text)
text = re.sub(r'\t+', '', text)
text = re.sub(r'^$\n+', '', text, flags=re.MULTILINE)
text = re.sub("[!@#$+%*:()'-]", '', text)
text = os.linesep.join([s for s in text.splitlines() if s])
text = "\n".join(list(OrderedDict.fromkeys(text.split("\n"))))
text = re.sub('(?m)^.{0,50}\n','',text)
# print( text )

# paragraphs = text.split('   ')
paragraphs = re.split(r'\s{3,}', text)
for paragraph in paragraphs:
    if paragraph!="":
        print(paragraph)
        print('\n')

