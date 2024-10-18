import base64
with open(r'C:\Users\Renuka\OneDrive\Desktop\output.txt', "rb") as File:
    str1= (File.read())
    imgdata = base64.b64decode(str1)
    filename = r'C:\Users\Renuka\OneDrive\Desktop\example.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)