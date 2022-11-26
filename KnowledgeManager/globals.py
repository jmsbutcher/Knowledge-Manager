
from pathlib import Path
import os

#ROOT = Path("C:/Users/James/Documents/Programming/KnowledgeManager")
ROOT = Path(os.getcwd()).parent
SOURCE_PATH = ROOT / "KnowledgeManager"
TEST_PATH = ROOT / "Tests"
DEFAULT_DOCUMENT_REPO_PATH = SOURCE_PATH / "km_Documents"
