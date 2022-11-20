# 11/19/22

from attribute import Attribute

class AttributeScheme:
    """ Contains list of attributes currently being used in the knowledge base"""

    #CATEGORY_IDENTIFIER = "#Category:"
    #KEYWORDS_IDENTIFIER = "#Keywords:"

    attributes = [
        Attribute("#Category:", "Category", "String"),
        Attribute("#Keywords:", "Keywords", "List")
    ]

    # def __init__(self):
    #     self.attributes = 

    
