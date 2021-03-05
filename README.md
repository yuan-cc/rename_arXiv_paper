## Rename and sort papers downloaded from arXiv
### Requirements
* Python 3.7 (recommended)
* Packages: arxiv, requests and pdfrw, which can be installed with pip,
``` pip intall arxiv requests pdfrw ```

### Run the code
Copy **`rename_arxiv.py`** to the default folder where arxiv papers are saved, usually `~/Downloads/` for MAC/Linux users. 

Before running the code, modify the following quantities in **`rename_arxiv.py`** 

* `new_dir:` directory to store the renamed papers. It may contain many subdirectories to categorize the papers by journals, years or keywords, etc. 
For example, I use Dropbox as my paper library and set `new_dir = "/Users/yuancc/Dropbox/"`. 

* `non_arxiv_dir` is the directory to store other pdf files. 

<img width="999" alt="Screen_Shot_2021-03-05_at_1 18 12_AM" src="https://user-images.githubusercontent.com/69713042/110075827-71342d80-7d51-11eb-88cc-49a96f9b9fee.png">


Run the code with python `python rename_arxiv.py` and it will scan the folder every `waittile` second(s) until stopped by `ctrl+C`. During the running time,
any arxiv papers saved to the folder will be renamed to the **`Author(Year)-Title.pdf`** format. Some options will be provided to drop the renamed paper.
You can select the existing subfolders under `new_dir` or create a new one by entering the corresponding indices. Pressing the `enter/return`
 key in this step will simply move the paper to `non_arxiv_dir`.
