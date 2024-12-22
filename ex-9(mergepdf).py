from PyPDF2 import PdfWriter
import os
pdf_directory = "Merge"
merger = PdfWriter()
# files=[file for file in os.listdir("Merge") if file.endswith(".pdf")]
files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
output_file = "merged-pdf.pdf"
merger.write(output_file)
# merger.write("merged-pdf.pdf")
merger.close()
# import os
# # os.rename("cluster/bout.txt","cluster/cluster.txt")
# # files = os.listdir("cluster")

# files = os.listdir("Merge")
# i = 1
# for file in files:
#   if file.endswith(".pdf"):
#     print(file)
#     os.rename(f"Merge/{file}", f"Merge/{i}.pdf")
#     i = i + 1