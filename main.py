#%%
import os
from PyPDF2 import PdfFileMerger
#%%
pdf_dir = input("Enter the folder of PDFs to merge:")

#%%
x = [a for a in os.listdir(pdf_dir) if a.endswith(".pdf")]
print('files found: \n{}'.format("\n".join(x)))
#%%

merger = PdfFileMerger()

for pdf in x:
    pdf_path = os.path.join(pdf_dir, pdf)
    merger.append(open(pdf_path, 'rb'))
#%%
out_path = os.path.join('out', 'result.pdf')
with open(out_path, "wb") as fout:
    merger.write(fout)
