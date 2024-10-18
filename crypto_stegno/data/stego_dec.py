from PIL import Image

def genData(data):
    # list of binary codes of given data
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')
    data = ''
    imgdata = iter(image.getdata())
    binstr = ''
    while (True):
        pixels = [value for value in imgdata.next()[:3] + imgdata.next()[:3] + imgdata.next()[:3]]
        for i in range(0, 8):
            if (pixels[i] % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        if (pixels[-1] % 2 != 0):
            data += chr(int(binstr, 2))
            if (data[-6:] == '#!@#$'):
                return data[:-6]
            binstr = ''

def main():
    print(":: Welcome to Steganography ::\n")
    sq = decode()
    print("Decoded word- " + sq)
    file = open("C:\\Users\\Renuka\\OneDrive\\Desktop\\New Text Document.txt", "w")
    file.write(sq)
    file.close()

if __name__ == '__main__':
    # Calling main function
    main()
