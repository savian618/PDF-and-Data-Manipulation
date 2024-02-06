import PyPDF2
import os
import time
import pandas as pd

def show_tree(bookmark_list, indent=0):
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call with increased indentation
            show_tree(item, indent + 4)
        else:
            index[item.title] = "{}".format(reader.get_destination_page_number(item)+1)
            

if __name__ =="__main__":
    start_time = time.time()
    docs = {}

    filedir = "M:\Mortgage Operations\interim_tools\idp_testing\Indexed Output Files - Step 3f"
    for file in os.listdir(filedir):
        if file.endswith(".pdf"):
            try:
                index = {}
                reader = PyPDF2.PdfReader("{}\{}".format(filedir, file))
                show_tree(reader.outline)
                docs[file] = index
            except:
                pass
    
    df =pd.DataFrame.from_dict(docs,orient='index')
    df.to_csv('bookmarks.csv')
    print("--- %s seconds ---" % (time.time() - start_time))
