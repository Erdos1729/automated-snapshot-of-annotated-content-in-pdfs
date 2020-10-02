"""
Created on Fri Aug 28 14:53:35 2020

@author: Erdos1729
"""

# loop through annotations of a page, change their author,
# make them 10% larger and save an image as PNG file
import fitz
import os
import pandas as pd


pdf_folder = './pdf'
input_file = './input/upload.csv'
coordinate_file = './input/sd_coordinates.csv'
output_folder = './output'

df = pd.DataFrame()
coordinates = []

############################################# Coordinates Extraction #############################################

print("Extracting annotation data from pdf files..........")

df1 = pd.read_csv(input_file, encoding='unicode-escape')
files = []
[files.append(x) for x in df1['pdf title'] if x not in files]

for item in files:
    file = pdf_folder + '/' + item + '.pdf'
    doc = fitz.open(file)
    n = doc.pageCount
    inst_counter = 0
    for x in range(0, n-1):
        page = doc[x]                                  # access page n (0-based)
        annot = page.firstAnnot                        # get first annotation
        #matrix = fitz.Matrix(1.1, 1.1)                # define matrix for scaling +10%
        y = 0                                          # counter for file idents

        while annot:                                   # loop through the page's annotations
            #pix = annot.getPixmap(matrix = matrix)    # picture map for the annot
            y += 1                                     # increase counter
            d = annot.info                             # get annot's info dictionary
            annot.setInfo(d)                           # update info dict in annot
            r = annot.rect                             # matrix #scale annot's rectangle
            coordinates.append(str(r))
            # print(r)
            annot.setRect(r)                           # store rect back in annot
            annot = annot.next                         # get next annot on page

# save coordinates to a new file:
df['coordinate'] = coordinates
df['title'] = df1['id']
df['pdf title'] = df1['pdf title']
df['page no.'] = df1['page no.']

df.to_csv(coordinate_file, index = False)

############################################# Snapshot of annotations #############################################

print("\nSaving snapshots..........")

dir1 = output_folder
dir = [dir1]

for x in dir:
    try:
        os.mkdir(x)
    except FileExistsError:
        print("Directory ", x, " already exists")

### READ IN PDF
dim = 0
df2 = pd.read_csv(coordinate_file, encoding = 'unicode-escape')
for n in range(len(df2)):
    file = pdf_folder + '/' + df2['pdf title'][n] + '.pdf'
    if "PPT" in file:
        dim = 1
    else:
        dim = 0.1
    # print(file)
    doc = fitz.open(file)
    inst_counter = 0
    pi = int(df2['page no.'][n]) - 1
    page = doc[pi]
    annot = page.firstAnnot

    while annot:
        annot = page.deleteAnnot(annot)

    five_percent_height = (page.rect.br.y - page.rect.tl.y) * dim
    target = df2['coordinate'][n]
    cor = target.split(", ")

    c1 = cor[0].replace("Rect(","")
    c2 = cor[1]
    c3 = cor[2]
    c4 = cor[3].replace(")","")
    r1 = fitz.Rect(c1, c2, c3, c4)

    highlight = page.addHighlightAnnot(r1)

    # Provide parameters to create a cropping box around the highlighted content
    tl_pt = fitz.Point(page.rect.tl.x, max(page.rect.tl.y, r1.tl.y - five_percent_height))
    br_pt = fitz.Point(page.rect.br.x, min(page.rect.br.y, r1.br.y + five_percent_height))
    hl_clip = fitz.Rect(tl_pt, br_pt)

    zoom_mat = fitz.Matrix(2, 2)
    # page.addRectAnnot(rect=hl_clip) # To add a black rectangle around the snapshot
    pix = page.getPixmap(matrix=zoom_mat, clip=hl_clip)
    pix.writePNG(dir1 + '/' + str(df2['title'][n]) + f".png")  # -hl{text_instances}

    doc.close()

print("\nProcess completed..........")