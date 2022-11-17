import json

filename = input('enter file name:')
def remove_punc(string):
    punc = '''!()-[]{};:'""\,<>./?@#$%^&*_~ “”’'''
    for e in string:
        if e in punc:
            string = string.replace(e, " ")
    return string

content=[]
try:
    with open(filename,'r') as f:
        data = f.read()
    with open(filename,"w+") as f:
        f.write(remove_punc(data))
        f.seek(0)
        data=f.readlines()
        for i in data:
            content.extend(i.split(" "))
    print(content)
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")


with open('abc.json','w') as f:
    json.dump(content,f)
print("json created")
