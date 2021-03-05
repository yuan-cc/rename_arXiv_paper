'''python 3.7'''
'''requirments: arxiv, shutil, pdfrw'''
import os
import arxiv
import time
import shutil
import requests
from pdfrw import PdfReader, PdfWriter
from glob import glob
import signal

new_dir = '/Users/yuancc/Dropbox/'  #destination folder
non_arxiv_dir = '/Users/yuancc/Downloads/other_pdf/' # to accommodate non-arxiv pdf files

waittime = 1 # wait [waittime] seconds between each loop

print()

def interrupted(signum, frame):
    print("Time out!")

signal.signal(signal.SIGALRM, interrupted)
TIMEOUT = 9999

def input_des():
    try:
            foo = int(input("Input the index >> "))
            return foo
    except:
            # timeout
            return -1



print('--------------------------------------')
print("Rename_arxiv_paper: running")
print("Scan the folder every "+str(waittime)+' second(s)')
print("Type \'ctrl-C\' to stop")
print('--------------------------------------')

try:
    while True:

        pdfs = [f for f in next(os.walk(os.getcwd()))[2] if f.endswith('.pdf')]
        if len(pdfs) > 0:
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            try:
                requests.head('https://arxiv.org/')
            except requests.ConnectionError:
                logging.error('failed to connect to arxiv.org')

        else:
            time.sleep(waittime)
            continue

        for pdf in pdfs:

            try:
                if(len(pdf) > 15):
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    shutil.move(pdf,non_arxiv_dir+pdf)
                    print('Moved to '+non_arxiv_dir)
                    time.sleep(waittime)
                    continue

                metadata = PdfReader(pdf).Info
                if '/arxiv_id' in metadata and '/updated' in metadata:
                    paper = arxiv.query(id_list=[metadata['/arxiv_id'][1:-1]])[0]
                    updated = metadata['/updated'][1:-1]
                else:
                    paper = arxiv.query(id_list=[pdf[:-4].split('v')[0]])[0]
                    updated = ''

                authors = paper['authors']
                title = ' '.join(paper['title'].split())
                year = str(paper['published_parsed'].tm_year)
                arxiv_id = paper['id'].split('/')[-1].split('v')[0]
                authors = paper['authors'][0].split(' ')[-1]
                title = title.replace(':', '').replace(',', '').replace('-',' ')
                pdf_name = authors + ' (' + year + ') - ' + title + '.pdf'

                print()
                print('Move'+'\033[1m' +'\"'+pdf_name+'\"'+'\033[0m'+' to')

                n=0
                print("\033[1m"+"0\033[0m: "+new_dir)
                subfolders = glob(new_dir+"*/")
                for item in subfolders:
                    n=n+1
                    print('\033[1m'+str(n)+'\033[0m: '+item)
                print('\033[1m'+str(n+1)+'\033[0m:'+' new folder')
                print('Return/enter key: '+non_arxiv_dir)

                signal.alarm(TIMEOUT)
                destination=input_des()
                signal.alarm(0)

                if(destination==0):
                    path=new_dir
                    shutil.move(pdf,path+pdf_name)
                    print("Moved to "+path)
                elif(destination>0 and destination <= len(subfolders)):
                    path = subfolders[destination-1]
                    shutil.move(pdf,path+pdf_name)
                    print("Moved to "+path)
                elif(destination == len(subfolders)+1):
                    print('Input the name of the new folder: (xxx/)')
                    newfolder=str(input() or " ")
                    path=new_dir+newfolder
                    os.mkdir(path)
                    shutil.move(pdf,path+pdf_name)
                    print("Moved to "+path)
                else:
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    shutil.move(pdf,non_arxiv_dir+pdf_name)
                    print('Moved to '+non_arxiv_dir)

            except:
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                shutil.move(pdf,non_arxiv_dir+pdf)
                print('Moved to '+non_arxiv_dir)

        time.sleep(waittime)

except KeyboardInterrupt:
    print(' ')

