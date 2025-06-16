from pypdf import PdfReader

def test():
    reader = PdfReader("tmp/Python Testing with Pytest (Brian Okken).pdf")
    print(len(reader.pages))

def test_second():
    reader = PdfReader("tmp/Python Testing with Pytest (Brian Okken).pdf")
    print(reader.pages[1].extract_text())



reader = PdfReader("tmp/Python Testing with Pytest (Brian Okken).pdf")
print(reader.pages[1].extract_text())
assert "Every precaution was taken in the preparation of this book." in reader.pages[1]