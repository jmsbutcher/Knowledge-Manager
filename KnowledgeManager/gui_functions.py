
from Utils.common_functions import extract_trailing_int

from DocumentManagement.document_creator import DocumentCreator

from globals import DEFAULT_DOCUMENT_REPO_PATH, doc_manager


def add_new_document():
    """ 
    Create a new empty text document with a default name and open it for editing
    """
    # Find an appropriate default name for the new document
    DEFAULT_DOCUMENT_PREFIX = "New Document"
    doc_names = doc_manager.get_list_of_names()

    # Extract the highest number following the default prefix
    highest_default_doc_number = 0
    for doc in doc_names:
        if DEFAULT_DOCUMENT_PREFIX in doc:
            num = extract_trailing_int(doc, DEFAULT_DOCUMENT_PREFIX)
            if num is not None:
                if num > highest_default_doc_number:
                    highest_default_doc_number = num
            else:
                highest_default_doc_number = 1
    
    default_doc_name = DEFAULT_DOCUMENT_PREFIX
    if highest_default_doc_number > 0:
        default_doc_name += str(highest_default_doc_number + 1)

    # Create a new empty text document
    doc_creator = DocumentCreator(DEFAULT_DOCUMENT_REPO_PATH)
    doc_creator.create_new_text_file_if_doesnt_exist(default_doc_name)

    doc_manager.load_documents()