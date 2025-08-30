import glob
import os

drawings = sorted(glob.glob("content/images/Drawings/*.png"))
max_digits = len(str(len(drawings))) # I like having leading zeroes in list

# grab all drawings in a list with ID, date, title and the file location
list_of_drawings = []
for i, drawing in enumerate(drawings):
    filename = os.path.basename(drawing)
    date = filename.split("_", 1)[0]
    drawing_name_extension = filename.split("_", 1)[1]
    drawing_name = drawing_name_extension.split(".png")[0]

    #drawings will be loaded from "output" folder
    drawing_location = "{static}/images/Drawings/%s" %filename
    
    list_of_drawings.append((str(i+1).zfill(max_digits), date, drawing_name.replace("_", " "), drawing_location))

# add content
page_content = ""
page_content += "Title: 04. Drawing Portfolio\n\n"
# leading paragraph
page_content += "This is a collection of digital drawings I've made. I hope I'll be able to expand it consistently :)\n\n"
for id, date, title, file_location in list_of_drawings[::-1]:
    page_content += "%s. [%s](%s) on %s\n" %(id, title, file_location, date)

with open("content/pages/Drawings.md", "w") as f:
    f.write(page_content)


