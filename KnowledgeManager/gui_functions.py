
from Utils.common_functions import extract_trailing_int

from DocumentManagement.document_creator import DocumentCreator
from DocumentManagement.document_editor import DocumentEditor
from DocumentManagement.document_manager import DocumentManager

from globals import DEFAULT_DOCUMENT_REPO_PATH


def add_new_document():
    """ 
    Create a new empty text document with a default name and open it for editing
    """
    # Find an appropriate default name for the new document
    DEFAULT_DOCUMENT_PREFIX = "New Document"
    doc_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
    doc_names = doc_manager.get_list_of_document_names()

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

    # Now open the new text document in default text editor
    doc_editor = DocumentEditor(DEFAULT_DOCUMENT_REPO_PATH)
    doc_editor.open_document_in_text_editor(default_doc_name)


# def format_attribute(attribute):
#     """ 
#     Convert document value into appropriate string representation

#     - Lists are converted into comma-separated values
#     - None is converted into an empty string
#     """
#     if attribute is None:
#         return ""
#     elif isinstance(attribute, list):
#         return ", ".join(attribute)
#     else:
#         return attribute
