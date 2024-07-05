from pathlib import Path
from datetime import datetime
import re
from typing import DefaultDict
import data_model



def read_raw_clippings(kindle_clippings_file_path: Path) -> str:
    try:
        with open(kindle_clippings_file_path, "r", ) as raw_clippings_file:
            raw_clippings_text = raw_clippings_file.read()

    except Exception as e:
        print(e)

    return raw_clippings_text


def get_book_details(raw_clippings: str):
    """

    :param raw_clippings:
    :return:
    """

    book_dict = {}  # to store infos like book name, author, last read
    book_contents_dict = DefaultDict[list]
    books = []
    kindle_clips_list = []
    # add the contents to a list
    raw_clippings_list = raw_clippings.split()
    for clip in kindle_clips_list:
        raw_clipping_list = clip.strip().split("\n")
        print(raw_clipping_list[-1])
        book_content = raw_clipping_list[-1]

        match = re.match(r'^(.*) \(([^)]+)\)$', raw_clipping_list[0])
        date_match = re.search(r'Added on (.+)', clip)

        if match:
            book_name = match.group(1)
            book_author = match.group(2)
            print(f"Book Name: {book_name}")
            print(f"Book Author: {book_author}")
            book_dict[book_name] = book_author
            book_contents_dict[book_name].append(book_content)
            # add the book name to a list and check if its already there
        else:
            print("No match found")
            print(raw_clipping_list)
        if date_match:
            date_str = date_match.group(1)
            date_obj = datetime.strptime(date_str, '%A, %d %B %Y %H:%M:%S')
            print(f"Date: {date_obj}")

        # books.append(data_model.BookDataModel(
        #         book_name=book_name,
        #         book_author=book_author,
        #         book_summaries=book_content,
        #         last_read=date_obj
        #     ))
