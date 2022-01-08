import pdfkit as pd 

url = input("copy your wiki URL and paste it here:  \n")

file_name = input("what do you want to name your file? \n")

file_name = file_name + ".pdf"

pd.from_url(url, file_name)