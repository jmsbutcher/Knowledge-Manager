# 10/29/22

from pathlib import Path

class Document:
    """ 
    Represents a text document
    
    _repo_path: path to the folder where the actual text document is stored
        e.g., "C://Documents/KnowledgeManager/my_repo/"

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

    def __init__(self, repo_path, name):
        self._repo_path = repo_path
        self.path = Path(repo_path) / name
        self.name = name
        self.contents = None
        self.category = None
        self.keywords = [] 


    
