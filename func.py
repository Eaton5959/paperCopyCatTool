def convertFunction(text):
    input_str = text

    out_str = input_str.replace(" ","").replace("\n","")
    print(out_str)
    return out_str


if __name__ == '__main__':
    convertFunction()