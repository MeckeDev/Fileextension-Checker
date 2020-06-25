import requests as r

data = r.get("https://www.webopedia.com/quick_ref/fileextensionsfull.asp").text

x = data.find('<h3>&nbsp; <a name="num"></a><span class="style3">Data File Formats and File Extensions - Complete List</span></h3>')
y = data.find('<p><span style="background-color: #ffff00;"><strong>Recommended Reading:</strong> <a href="https://www.webopedia.com/quick_ref/fileextensions.asp">An Introduction to Data File Formats and Their File Extensions</a></span></p>')

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

    print(f"The extension of the File is: {get_ext(filename)}")
