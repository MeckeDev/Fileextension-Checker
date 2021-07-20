import requests as r

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
data = r.get("https://www.webopedia.com/quick_ref/fileextensionsfull.asp", headers=headers).text

x = data.find('<h3>  <a name="num"></a><span class="style3">Data File Formats and File Extensions &#8211; Complete List</span></h3>')
y = data.find('<td class="style8"><a href="https://www.webopedia.com/reference/fileextensionsnumber/" title="File Extensions that Begin with a Number">Number</a>')

formats = data[x:y].split("<tr>")
all_formats = {}

for i in formats:
    a = i.split('valign="top">')
    try:
        b = a[1].split('</td')[0]
        c = a[2].split('</td>')[0]

        if len(b) > 0 and len(c) > 0:

            all_formats[b] = c

    except:
        pass

def get_ext(file):

    try:
        l = len(file.split("."))
        extension = all_formats[f'.{file.split(".")[l-1]}']

        return extension

    except:
        return f"{file} is not a valid filename"

print(len(all_formats))

while True:

    filename = input("Input the Filename: ")

    if filename == "exit" or filename == "quit":
        break

    print(f"The extension of the File is: {get_ext(filename)}\n")
