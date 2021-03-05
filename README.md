## Rename and sort the papers downloaded from arXiv
### Requirements
* Python 3.7 (recommended)
* Packages: arxiv, requests and pdfrw, which can be installed with pip,
``` pip intall arxiv requests pdfrw ```

### Run the code
Copy **`rename_arxiv.py`** to the default folder where arxiv papers are saved, usually `~/Downloads/` for MAC/Linux users. 

Before running the code, modify the following quantities in **`rename_arxiv.py`** 

* `new_dir:` directory to store the renamed papers. It may contain many subdirectories to categorize the papers by journals, years or keywords, etc. 
For example, I use Dropbox as my paper library and I set `new_dir = "/Users/yuancc/Dropbox/"`. 

* `non_arxiv_dir` is the directory to store other pdf files. 

Run the code with python `python rename_arxiv.py` and the code will scan the folder every `waittile` second(s) until stopped by `ctrl+C`. During the running time
any arxiv paper saved to the folder will be renamed to the **`Author(Year)-Title.pdf`** format. The code will also ask you where to drop the renamed paper.
You can select the existing subfolders under `new_dir` or create a new one by inputting the corresponding index. Pressing the `enter/return`
 key in this step will simply move the paper to `non_arxiv_dir`.
