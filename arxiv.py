import os
import arxiv
import time
import shutil
import requests
import threading
from threading import Timer
from pdfrw import PdfReader, PdfWriter
from glob import glob

new_path = '/Users/yuancc/Dropbox/'

target = glob('*.pdf')


pdfs = [f for f in next(os.walk(os.getcwd()))[2] if f.endswith('.pdf')]
if len(pdfs) > 0:
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    try:
        requests.head('https://arxiv.org/')
    except requests.ConnectionError:
        logging.error('failed to connect to arxiv.org')
        raise SystemExit(0)
else:
    print('there are no pdf files in the current directory...')
    raise SystemExit(0)
for pdf in pdfs:
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
    print('Move '+pdf_name+' to')
    n=0
    print("(0): "+new_path)
    subfolders = glob(new_path+"*/")
    for item in subfolders:
        n=n+1
        print('('+str(n)+'): '+item)
    print('('+str(n+1)+'):'+' new folder')
    prompt = "Integer>> "
    destination = int(input('Integer>>') or 0)
    if(destination==0):
        path=new_path
        shutil.move(pdf,path+pdf_name)
    elif(destination>0 and destination <= len(subfolders)):
        path = subfolders[destination-1]
        shutil.move(pdf,path+pdf_name)
    elif(destination == len(subfolders)+1):
        print('Input the name of the new folder: ')
        newfolder=str(input() or " ")
        path=new_path+newfolder
        os.mkdir(path)
        shutil.move(pdf,path+pdf_name)
    else:
        print('remove '+pdf_name)
        os.remove(pdf)

