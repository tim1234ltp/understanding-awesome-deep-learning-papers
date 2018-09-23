import os
from os.path import isfile, join
from typing import List

# path to pdftotext.exe
PTTPATH = "pdftotext.exe"


def pdf_to_text(filename: str):
    command = PTTPATH + ' ' + '"' + filename + '"'
    os.system(command)


def get_list_of_papers()-> List:
    papers_path = []
    for sub in os.listdir("F:\personal project\ML\papers"):
        sub_category = "F:\personal project\ML\papers\\" + sub
        for f in os.listdir(sub_category):
            paper = join(sub_category, f)
            if isfile(paper):
                papers_path.append(paper)
    return papers_path


if __name__ == "__main__":
    list_of_paper = get_list_of_papers()
    for p in list_of_paper:
        pdf_to_text(p)
