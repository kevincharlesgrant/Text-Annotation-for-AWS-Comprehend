#https://automatetheboringstuff.com/chapter13/
#write docx file to txt
directory = #filepath
for filename in os.listdir(directory):
    if filename.endswith(\".docx\"):
        fulltext = getText(filename)
        filename.rsplit('.')
        f= open(filename+\".txt\",\"w+\")
        f.write(fulltext)
    else:
        continue