# 10/9/22

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagement.document_manager import DocumentManager
from KnowledgeManager.DocumentManagement.document_creator import DocumentCreator
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentManager(TestBase):

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
        

    def test_search_for_document_returns_all_docnames_with_substr(self):
        """ 
        Test whether the Document Manager's search_for_document function
        returns a list of document names that contain the search substring.
        """
        # Create a temporary document folder
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)

        # Create two test documents
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc2")
        doc_creator.create_new_text_file_if_doesnt_exist("another_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("andanother")

        # Create the document manager
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)


        # Check if search_for_document finds the two correct documents
        search_result_names = doc_manager.search_for_document("doc1")
        self.assertTrue("test_doc1" in search_result_names)
        self.assertTrue("another_doc1" in search_result_names)

        # Check if search_for_document returns an empty list when not found
        search_result_names = doc_manager.search_for_document("doc3")
        self.assertTrue(len(search_result_names) == 0)


    def test_extract_doc_name_from_path(self):
        """ Ensure doc name extracted from path, with extension removed """
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        path = TEST_DOCUMENT_REPO_PATH / "test_document.txt"
        extracted_doc_name = doc_manager._extract_doc_name_from_path(path)
        self.assertEqual(extracted_doc_name, "test_document")


    def test_extract_doc_name_from_path_with_prefix(self):
        """ Ensure doc name extracted from path, with extension included """
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        path = TEST_DOCUMENT_REPO_PATH / "test_document.txt"
        extracted_doc_name = doc_manager._extract_doc_name_from_path( \
            path, remove_extension=False)
        self.assertEqual(extracted_doc_name, "test_document.txt")


    def test_load_document_category_returns_category(self):
        """ Ensure extracts string from document after category identifier """
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc_path = TEST_DOCUMENT_REPO_PATH / "test_doc.txt"
        with open(doc_path, "w") as doc:
            identifier = DocumentManager.CATEGORY_IDENTIFIER
            doc.write(identifier + "TestCategory")
        
        category = doc_manager._load_doc_category(doc_path)
        self.assertEqual(category, "TestCategory")


    def test_load_document_category_returns_none_when_no_identifier(self):
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc_path = TEST_DOCUMENT_REPO_PATH / "test_doc.txt"
        with open(doc_path, "w") as doc:
            doc.write("so9wqi12\n2193ij23\ni1oci")
        
        category = doc_manager._load_doc_category(doc_path)
        self.assertIsNone(category)


    def test_load_document_category_returns_none_when_value_absent(self):
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc_path = TEST_DOCUMENT_REPO_PATH / "test_doc.txt"
        with open(doc_path, "w") as doc:
            identifier = DocumentManager.CATEGORY_IDENTIFIER
            doc.write(identifier + "\nso9wqi12\n2193ij23\ni1oci")
        
        category = doc_manager._load_doc_category(doc_path)
        self.assertIsNone(category)


    def test_load_document_keywords_returns_keywords(self):
        """ 
        Ensure extracts list of strings from document after keyword identifier
        """
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc_path = TEST_DOCUMENT_REPO_PATH / "test_doc.txt"
        with open(doc_path, "w") as doc:
            identifier = DocumentManager.KEYWORDS_IDENTIFIER
            doc.write(identifier + " testkeyword1, Test Keyword 2, k w 3")
        
        keywords = doc_manager._load_doc_keywords(doc_path)
        self.assertEqual(keywords[0], "testkeyword1")
        self.assertEqual(keywords[1], "Test Keyword 2")
        self.assertEqual(keywords[2], "k w 3")


    def test_load_document_from_path_loads_correctly(self):
        """ Test that a correctly loaded document object is returned """
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc_path = TEST_DOCUMENT_REPO_PATH / "test_doc.txt"
        with open(doc_path, "w") as doc:
            cat_identifier = DocumentManager.CATEGORY_IDENTIFIER
            kw_identifier = DocumentManager.KEYWORDS_IDENTIFIER
            doc.write(cat_identifier + " testcategory")
            doc.write(kw_identifier + " kw1, kw2, kw3")
            doc.write("\n...random contents...")
            doc.write("\n...more random contents...")
        
        doc =  doc_manager._load_document_from_path(doc_path)
        self.assertEqual(doc.name, "test_doc")
        self.assertEqual(doc._repo_path, TEST_DOCUMENT_REPO_PATH)
        self.assertEqual(doc.contents, 
            "...random contents...\n...more random contents...")


    def test_get_document_by_name_returns_document(self):
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        doc = doc_manager.get_document_by_name("test_doc1")
        self.assertEquals(doc.name, "test_doc1")


    def test_get_document_by_name_when_doesnt_exist_return_exception(self):
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)
        #doc = doc_manager.get_document_by_name("test_doc2")
        self.assertRaises(FileNotFoundError, doc_manager.get_document_by_name, "test_d")


    def test_filter_documents_by_category_returns_correct_documents(self):
        # Create two test documents
        # - Need to do this first so the document_hander_base can create the 
        #   document repo. Otherwise, can't manually write to the documents
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc2")

        # Add categories tags to the test documents
        cat_identifier = DocumentManager.CATEGORY_IDENTIFIER
        doc_path1 = TEST_DOCUMENT_REPO_PATH / "test_doc1.txt"
        with open(doc_path1, "w") as doc:
            doc.write(cat_identifier + " testcategory1")
            doc.write("\n...random contents...")

        doc_path2 = TEST_DOCUMENT_REPO_PATH / "test_doc2.txt"
        with open(doc_path2, "w") as doc:
            doc.write(cat_identifier + " testcategory2")
            doc.write("\n...random contents...")

        # Now use a document manager to filter the documents by category
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)

        matching_category_documents = \
            doc_manager.filter_documents_by_category("testcategory1")
        self.assertEqual(matching_category_documents[0].name, "test_doc1")

        matching_category_documents = \
            doc_manager.filter_documents_by_category("testcategory2")
        self.assertEqual(matching_category_documents[0].name, "test_doc2")


    def test_filter_documents_by_keyword_returns_correct_documents(self):
        # Create test documents
        # - Need to do this first so the document_hander_base can create the 
        #   document repo. Otherwise, can't manually write to the documents
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc1")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc2")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc3")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc4")
        doc_creator.create_new_text_file_if_doesnt_exist("test_doc5")

        # Add keywords to the test documents
        keywords_identifier = DocumentManager.KEYWORDS_IDENTIFIER
        doc_path1 = TEST_DOCUMENT_REPO_PATH / "test_doc1.txt"
        with open(doc_path1, "w") as doc:
            doc.write("\n...random contents...")    # No keywords

        doc_path2 = TEST_DOCUMENT_REPO_PATH / "test_doc2.txt"
        with open(doc_path2, "w") as doc:
            doc.write(keywords_identifier)          # Only keyword identifier
            doc.write("\n...random contents...")

        doc_path3 = TEST_DOCUMENT_REPO_PATH / "test_doc3.txt"
        with open(doc_path3, "w") as doc:
            doc.write(keywords_identifier + " kw1") # 1 keyword
            doc.write("\n...random contents...")

        doc_path4 = TEST_DOCUMENT_REPO_PATH / "test_doc4.txt"
        with open(doc_path4, "w") as doc:
            doc.write(keywords_identifier + " kw2") # different keyword
            doc.write("\n...random contents...")

        doc_path5 = TEST_DOCUMENT_REPO_PATH / "test_doc5.txt"
        with open(doc_path5, "w") as doc:
            doc.write(keywords_identifier + " kw2, kw3") # 2 keywords
            doc.write("\n...random contents...")

        # Now use a document manager to filter the documents by keyword
        doc_manager = DocumentManager(TEST_DOCUMENT_REPO_PATH)

        # Should have no matches
        matching_kw_documents = \
            doc_manager.filter_documents_by_keyword("nonexistent_keyword")
        self.assertEqual(len(matching_kw_documents), 0)

        # Should have 1 match
        matching_kw_documents = \
            doc_manager.filter_documents_by_keyword("kw1")
        self.assertEqual(len(matching_kw_documents), 1)
        self.assertEqual(matching_kw_documents[0].name, "test_doc3")

        # Should have 1 match
        matching_kw_documents = \
            doc_manager.filter_documents_by_keyword("kw3")
        self.assertEqual(len(matching_kw_documents), 1)
        self.assertEqual(matching_kw_documents[0].name, "test_doc5")

        # Should have 2 matches
        matching_kw_documents = \
            doc_manager.filter_documents_by_keyword("kw2")
        matching_kw_doc_names = [d.name for d in matching_kw_documents]
        self.assertEqual(len(matching_kw_documents), 2)
        self.assertTrue("test_doc4" in matching_kw_doc_names)
        self.assertTrue("test_doc5" in matching_kw_doc_names)

        # Should have 1 match
        matching_kw_documents = \
            doc_manager.filter_documents_by_keyword(["kw2", "kw3"])
        self.assertEqual(len(matching_kw_documents), 1)
        self.assertTrue("test_doc5" in matching_kw_doc_names)
