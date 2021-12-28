import os
from classes.heading import Heading

class Chapter(object):
    def __init__(self, attributes, included, date_param):
        self.included = included
        self.goods_nomenclature_item_id = attributes["goods_nomenclature_item_id"]
        self.description = attributes["formatted_description"]
        self.date_param = date_param
        
        self.get_headings()
        
    def get_headings(self):
        # Get data for the included headings
        self.headings = []
        for item in self.included:
            if item["type"] == "heading":
                heading = Heading(item["attributes"], self.date_param)
                self.headings.append(heading)
