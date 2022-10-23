# 10/9/22

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagers.document_manager import DocumentManager
from KnowledgeManager.DocumentManagers.document_creator import DocumentCreator
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentManager(TestBase):

    def test_create_document_manager(self):
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        self.assertTrue(True)


    def test_document_manager_loads_list_of_documents(self):
        """ Test that document manager loads all documents on init """
        # Create a temporary document folder
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)

        # Create two test documents
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc2")

        # Create the document manager
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)

        # Check if document manager loaded the two documents
        self.assertEqual(len(doc_manager._list_of_documents), 2)

    
    def test_document_manager_lists_document_names_in_repo(self):
        # Create a temporary document folder
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)

        # Create two test documents
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc2")

        # Create the document manager
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)

        document_names = doc_manager.get_list_of_document_names()

        # Check if document manager loaded the two documents
        self.assertEqual(document_names[0], "test_doc1")
        self.assertEqual(document_names[1], "test_doc2")
        
