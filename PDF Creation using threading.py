import threading
import PyPDF2
import os
import sys
import time
import pandas as pd
import math
import traceback

def pdf_maker(key_path):
    loan_folder = "M:\Mortgage Operations\interim_tools\IDP_testing\Input Files\All Packages for Test"
    keys = pd.read_csv(key_path)
    keys['Child'] = keys['Child'].apply(lambda x: x.lower() if isinstance(x, str) else x)
    priority = keys['Child'].tolist()
    df = pd.read_csv('Index.csv')
    df['doc_label'] = df['doc_label'].apply(lambda x: x.lower() if isinstance(x, str) else x)
    for key in priority:
        start_time = time.time()
        merger = PyPDF2.PdfMerger()
        print("Starting {}...".format(key))
        try:
            result = df[df['doc_label'] == key]
            for index, row in result.iterrows():
                page = math.floor(row['page_number']-1)
                loan = math.floor(row['package_id'])
                file = '{}\{}.pdf'.format(loan_folder,loan)
                try:
                    merger.append(file, outline_item="{}-{}".format(loan, page+1), import_outline=False, pages=(page, page+1))
                except:
                    pass
            output_file = "M:\Mortgage Operations\interim_tools\IDP_testing\Input Files\Label Results\{}.pdf".format(key)
            print("{} Writing...".format(key))
            merger.write(output_file)
            print("{} Done".format(key))
            merger.close()
        except Exception as e:
            print("{} Failed".format(key))
            print(traceback.format_exc())

        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ =="__main__":
    t1 = threading.Thread(target=pdf_maker, args=("Key1.csv",))
    t2 = threading.Thread(target=pdf_maker, args=("key2.csv",))
    t3 = threading.Thread(target=pdf_maker, args=("Key3.csv",))
    t4 = threading.Thread(target=pdf_maker, args=("key4.csv",))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("PDFs All Created!")