# 10/9/22

from KnowledgeManager.DocumentManagers.document_manager import DocumentManager
from KnowledgeManager.DocumentManagers.document_creator import DocumentCreator
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentManager(TestBase):
    
    def setUp(self):
        TestBase.setUp(self)
    

    #------------------------------------------------------------------------------------


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
        
