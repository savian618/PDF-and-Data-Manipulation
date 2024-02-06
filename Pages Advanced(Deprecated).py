import PyPDF2
import os
import time
import pandas as pd
import fitz


def get_page(f1, f2):
    pages = {'File1: Title':[],
             'File1: Page': [],
             'File2: Title':[],
             'File2: Page': [],
             'File1 Matching Page': []}
    df = pd.DataFrame(pages)
    pdf1 =  fitz.open(f1)
    pdf2 =  fitz.open(f2)
    for i in range(pdf1.page_count):
        data = []
        page1 = pdf1.load_page(i)
        lines1 = page1.get_text().splitlines()
        page2 = pdf2.load_page(i)
        lines2 = page2.get_text().splitlines()
        try:
            data.append(lines1[0])
            data.append(i+1)
        except:
            data.append("No Title")
            data.append(i+1)
        try:
            data.append(lines2[0])
            data.append(i+1)
        except:
            data.append("No Title")
            data.append(i+1)
        for j in range(pdf2.page_count):
            matchpage = pdf2.load_page(j)
            if page1.get_text() == matchpage.get_text():
                data.append(j+1)
                break
        df.loc[len(df.index)] = data
    return df


start_time = time.time()

file1 = "M:\Mortgage Operations\interim_tools\idp_testing\Indexed Output Files - Step 3f\8204973370_20230808122907258044 - Indexed Response.pdf"
file2 = "M:\Mortgage Operations\interim_tools\idp_testing\Assembler Output Files - Step 1e\8204973370_20230808122907258044 - Assembler Response.pdf"

result = get_page(file1, file2)
print("Done!")
result.to_csv('Pages Advanced.csv')
print("--- %s seconds ---" % (time.time() - start_time))