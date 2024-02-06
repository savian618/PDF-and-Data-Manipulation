import PyPDF2
import os
import time
import pandas as pd

if __name__ =="__main__":
    start_time = time.time()
    i =0
    docs = {}

    filedir = "M:\Mortgage Operations\interim_tools\idp_testing\Indexed Output Files - Step 3f"
    results = open('Bookmark.txt', 'w')
    for file in os.listdir(filedir):
        if file.endswith(".pdf"):
            try:
                reader = PyPDF2.PdfReader("{}\{}".format(filedir, file))
                docs[file] = len(reader.pages)
            except:
                pass
    
    df = pd.DataFrame.from_dict(docs, orient='index')
    df.to_csv('Total.csv')

    print("--- %s seconds ---" % (time.time() - start_time))
