# understanding-awesome-deep-learning-papers
This a try to do topic modellng on best 100 papers from github repo [awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers).

From the repo, we should have 100 papers but during the [crawling with script](fetch_papers.py),
the access towards one of them (`Human-level control through deep reinforcement learning`) is blocked. <br>

Then, a [script](parse_pdf_to_text.py) and [pdftotext](https://www.xpdfreader.com/pdftotext-man.html) is used to
parse pdfs to plain texts. <br>
In [find_topics.py](find_topics.py), we concatenate all plain texts to `paper.txt` which is of size 4 MB.
This means there is about 4000000 characters in the data. <br>
The `gensim` is used as it is tailored for topic modelling. The findings are visualized by `pyLDAvis` and stored as `.html`.
