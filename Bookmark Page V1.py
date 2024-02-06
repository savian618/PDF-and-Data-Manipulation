import PyPDF2
import os
import time
import pandas as pd

"""
Method: show_tree
Parameters: bookmark_list
Description:  takes in a list of bookmarks and adds each bookmark with its corresponding page number into a dictionary
"""
def show_tree(bookmark_list):
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call to iterate within the child bookmarks
            show_tree(item)
        else:
            index[item.title] = "{}".format(reader.get_destination_page_number(item)+1)
            

if __name__ =="__main__":
    start_time = time.time()
    #The directory to be searched
    filedir = "M:\\Mortgage Operations\\interim_tools\\IDP_testing\\Indexed Output Files - Step 3f\\IDP TNT Testing\\New IDP Indexed Packages"
    for folder in os.listdir(filedir):
        path = "{}\\{}".format(filedir, folder)       
        #dictionary of the following format {file name: {bookmark:page number}}
        docs = {}
        for file in os.listdir(path):
            if file.endswith(".pdf"):
                try:
                    #dictionary of the following format {bookmark:page number}
                    index = {}
                    reader = PyPDF2.PdfReader("{}\{}".format(path, file))
                    show_tree(reader.outline)
                    docs[file] = index
                except:
                    pass
        #converts the docs dictionary to a dataframe
        df =pd.DataFrame.from_dict(docs,orient='index')
        #outputs the dataframe as an csv with the name of the folder(should be loan number)
        df.to_csv('{}.csv'.format(folder))
        print("--- %s seconds ---" % (time.time() - start_time))