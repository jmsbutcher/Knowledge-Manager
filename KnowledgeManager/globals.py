
from pathlib import Path
import os

from DocumentManagement.document_manager import DocumentManager


ROOT = Path(os.getcwd()).parent
SOURCE_PATH = ROOT / "KnowledgeManager"
TEST_PATH = ROOT / "Tests"
DEFAULT_DOCUMENT_REPO_PATH = SOURCE_PATH / "repo"

# ROOT = Path(os.getcwd())
# print(ROOT)
# SOURCE_PATH = ROOT / "KnowledgeManager"
# TEST_PATH = ROOT / "Tests"
# DEFAULT_DOCUMENT_REPO_PATH = ROOT / "repo"

print(DEFAULT_DOCUMENT_REPO_PATH)

doc_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
