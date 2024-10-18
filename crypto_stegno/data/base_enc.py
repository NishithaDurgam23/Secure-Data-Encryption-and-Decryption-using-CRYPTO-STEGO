import base64

with open(r'C:\Users\Renuka\OneDrive\Desktop\example.jpg', "rb") as file:
    str1 = base64.b64encode(file.read())
    print(str1)
    filename = r'C:\Users\Renuka\OneDrive\Desktop\output.txt'

    # we are considering a file to store the string.
    with open(filename, 'wb') as f:
        f.write(str1)

