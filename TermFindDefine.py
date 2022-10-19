from PyPDF2 import PdfFileReader, PdfFileWriter
import re
#NAME PDF chem.pdf
file_path = 'chem.pdf'
pdf = PdfFileReader(file_path)
#create and format chem comp.txt

with open('chem comp.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)

        try: 
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()

ChemTXT = open("chem comp.txt", "r").readlines()
Terms = []#Vocab to be defined
for ans in ChemTXT:
    if ans.startswith("Word:"):
        Terms.append(ans[5:])    
    elif ans.startswith("@ S. Carmichael 2015  Word:"):
        Terms.append(ans[27:])
    elif ":" not in ans and "-" not in ans and "Page" not in ans and "Picture" not in ans and "Definition" not in ans: 
        Terms.append(ans)
    elif 'Week' in ans:
        Terms.append("NxtPg")
    #find the term lines

z = 0
for m in range(len(Terms)):
    Terms[z] = Terms[z].replace("\n", "")
    #remove \n
    Terms[z] = re.sub("^\\s+|\\s+$", "", Terms[z])
        #remove spaces at end
    Terms[z] = Terms[z].replace(' ', '%20')
    #change space into %20 for merriam formatting
    Terms[z] = Terms[z].replace("’", '%27')
    #replace the '
    if Terms[z].islower() is True:
        Terms[z] = Terms[z - 1] + "%20" + Terms[z]
        #remove those pesky 2 line definitions
    z += 1

print(Terms)

#merriam webster api
defs = [] 
import requests
wordnum = 1
for i in Terms:
    if "NxtPg" not in i:
        link = 'https://dictionaryapi.com/api/v3/references/sd4/json/'+ i +'?key=097ffc46-e2c1-462e-9e74-d2fcef820b85'
        r = requests.get(link)
        j = r.text
        q = j.split(',')
        if '"shortdef"' in j: 
            defnum = 0
            for a in q:
                if a.startswith('"shortdef"'):
                    defs.append(a[12:])
                    defnum += 1
    

            tdefnum = defnum
            if tdefnum > 1:
                while tdefnum >= 1:
                    print(tdefnum, defs[-tdefnum])
                    tdefnum -= 1
                print("Word: ", i)
                whichdef  = int(input("(1 - 9) Which definiton most fits the word: "))

                for i in defs[-defnum:]:
                    if i != defs[len(defs) - whichdef]:
                        defs.remove(i)
        

            print("----------------------------------------------------------------------------------------NEXTTWORD")
    
        else:
            defs.append("NA")
        wordnum += 1

print("\n\n ----------------------------------------------------------------------------------------\n\n")
for i in defs :
    print(i +'\n')
    print("-----------------------------------------------------------------------------------------------") 
#ADDD CRAIG!!!!!!!!!!!!!!


i = Terms.count("NxtPg") - 1

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder
from PyPDF2 import PdfFileMerger
# Fill the writer with the pages you want
import os
path = 'C:\\programming\\newproject'
RESOURCE_ROOT = 'C:\\programming\\newproject'
pdf_path = 'C:\\programming\\newproject'
for i in defs:
    PGN = 0
    pdf_path = os.path.join(RESOURCE_ROOT, "chem.pdf")
    reader = PdfReader(pdf_path)
    page = reader.pages[PGN]
    writer = PdfWriter() 
    writer.add_page(page)

    g = 0
    for i in defs:
        while len(i.split('\n')) > 30:
            i = defs[g] = re.sub("\s", "\n", i[:30], -1)
        g += 1
    # Create the annotation and add it
    def boxMake(BotY, TopY, PgNum, TWrm):
        annotation = AnnotationBuilder.free_text(
            #after 32 char skip make new linec
            TWrm,
            rect=(30, BotY, 252, TopY),
            #(left)x, (bottom)y, (right)x, (top)y
            font="Arial",
            bold=True,
        italic=True,
            font_size="16pt",
            font_color="000000",
            border_color="cdcdcd",
            background_color="cdcdcd",
        )
        writer.add_annotation(page_number=PgNum, annotation=annotation)
    n = 0
    Pg = -1
    
    if "NxtPg" in Terms[n]:
        Pg += 1
        n = 0
        BTY = 535
        TPY = 700

    boxMake(BTY, TPY, Pg, i)
    
    if n == 1:
        BTY -= 240
        TPY -= 215
    if n == 2:
        BTY -= 220
        TPY -= 240
    n += 1
    Temps = "Compchem" + str(PGN + 1) + ".pdf"
    with open(Temps, "wb") as fp:
        writer.write(fp)
    PGN += 1


pdf_merger = PdfFileMerger()

i = Terms.count("NxtPg")

for n in range(i):
    pdf_merger.append("Compchem" + str(n + 1) +".pdf")

with open(paths.abspath('FinalChem.pdf'), 'wb') as append_pdf:
    pdf_merger.write(append_pdf)

pdf_merger2 = PdfFileMerger()

files = [file for file in lisdir('.') if path.isfile(file) and file.endswith(".pdf")]

for file in files:
    print(file)
    pdf_merger2.append(file)

with open(path.abspath('FinalChem.pdf'), 'wb') as append_all_pdf:
    pdf_merger2.write(append_all_pdf)


#USE THE .JUST to ADD Links



