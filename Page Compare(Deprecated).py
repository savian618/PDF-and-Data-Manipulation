import PyPDF2
import os
import time
import pandas as pd
import fitz


def get_page(f1, f2):
    pages = {'File1: Page': [],
             'File2 Matching Page': []}
    df = pd.DataFrame(pages)
    pdf1 =  fitz.open(f1)
    pdf2 =  fitz.open(f2)
    for i in range(pdf1.page_count):
        page1 = pdf1.load_page(i)
        for j in range(pdf2.page_count):
            page2 = pdf2.load_page(j)
            if page1.get_text() == page2.get_text():
                df.loc[len(df.index)] = [i+1, j+1]
                break
    return df


start_time = time.time()

file1 = "M:\Mortgage Operations\interim_tools\idp_testing\Indexed Output Files - Step 3f\8204973370_20230808122907258044 - Indexed Response.pdf"
file2 = "M:\Mortgage Operations\interim_tools\idp_testing\Assembler Output Files - Step 1e\8204973370_20230808122907258044 - Assembler Response.pdf"

result = get_page(file1, file2)

result.to_csv('page compare.csv', index=False)

print("--- %s seconds ---" % (time.time() - start_time))