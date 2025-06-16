from zipfile import ZipFile

def test_arch():
    with ZipFile ("tmp/hello.zip") as zip_file:
        print(zip_file.namelist())
        text = zip_file('Hello.txt')
        print(text)
        #расспаковка
        zip_file.extract('Hello.txt', path="tmp")
