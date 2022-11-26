# 10/29/22

from pathlib import Path

class Document:
    """ 
    Represents a text document

    path: the path to the text document
        e.g., "C:/Documents/my_document.txt"

    name: the name of the text document
        e.g., "my_document"

    contents: the main contents of the text document, not including headers
        e.g., "Shopping list\n 1. Milk\n 2. Eggs"

    category: a string meant to represent one of a set of categories,
        extracted from the text document header
        e.g., "Category: Lists"

    keywords: a list of strings meant to help sort and group documents
        extracted from the text document header
        e.g., "Keywords: Shopping, Disposable"

    """
    def __init__(self, filepath):
        self.path = Path(filepath)
        self.name = None
        self.contents = None
        self.category = None
        self.keywords = [] 
    
