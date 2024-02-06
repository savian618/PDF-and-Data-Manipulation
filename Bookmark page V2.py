import PyPDF2
import os
import time
import pandas as pd

"""
Method: show_tree
Parameters: bookmark_list
Description:  takes in a list of bookmarks and adds each bookmark with its corresponding page number into a dataframe
"""
def show_tree(bookmark_list):
    for i in range(len(bookmark_list)):
        if isinstance(bookmark_list[i], list):
            for item in bookmark_list[i]:
                #a list to add values to dataframe
                data =[]
                #appends the file name we are searching
                data.append(file)
                #appends the parent bookmark
                data.append(bookmark_list[i-1].title)
                #appends the child bookmark
                data.append(item.title)
                #appends the page loaction of the child bookmark
                data.append(reader.get_destination_page_number(item)+1)
                df.loc[len(df.index)] = data

            

if __name__ =="__main__":
    start_time = time.time()
    #directory to be searched
    filedir = r"M:\Mortgage Operations\interim_tools\IDP_testing\Indexed Output Files - Step 3f\IDP TNT Testing\New IDP Indexed Packages\8205460134"
    #dateframe structure
    bookmark = {'File': [],
                'Parent Bookmark':[],
                'Child Bookmark': [],
                'Page':[]}
    df = pd.DataFrame(bookmark)
    for file in os.listdir(filedir):
        if file.endswith(".pdf"):
            try:
                reader = PyPDF2.PdfReader("{}\{}".format(filedir, file))
                show_tree(reader.outline)
            except:
                pass
    df.to_csv('bookmarks.csv')
    print("--- %s seconds ---" % (time.time() - start_time))
