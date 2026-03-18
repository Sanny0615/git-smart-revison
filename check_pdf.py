import pypdf

reader = pypdf.PdfReader("data/pdfs/Digital Logic!.pdf")
page = reader.pages[2]
text = page.extract_text()
print("Page 3 text:")
print(text[:500])