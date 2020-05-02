from docx import Document

document = Document("documents/LearningParseStructures.docx")
for para in document.paragraphs:
    print(para.text)