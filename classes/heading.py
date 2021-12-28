import os
import sys
import requests
from dotenv import load_dotenv

from classes.commodity import Commodity


class Heading(object):
    def __init__(self, attributes, date_param):
        load_dotenv('.env')
        self.root_url = os.getenv('ROOT_URL')
        self.goods_nomenclature_item_id = attributes["goods_nomenclature_item_id"]
        self.description = attributes["formatted_description"]
        self.date_param = date_param
        
        self.cleanse_description()
        self.declarable = attributes["declarable"]
        self.commodities = []
        self.hierarchy = []
        if not self.declarable:
            self.get_commodities()
            self.get_hierarchy()

    def cleanse_description(self):
        self.description = self.description.replace("\u00a0", "&nbsp;")
        self.description = self.description.replace("\u00e9", "&eacute;")

    def get_commodities(self):
        heading_id = self.goods_nomenclature_item_id[0:4]
        # print(heading_id)
        url = self.root_url + "headings/" + heading_id + self.date_param
        response = requests.get(url)
        if response:
            json = response.json()
            included = json["included"]
            for item in included:
                if item["type"] == "commodity":
                    commodity = Commodity(item["attributes"], self.description)
                    self.commodities.append(commodity)

    def get_hierarchy(self):
        commodity_count = len(self.commodities)
        for i in range(commodity_count - 1, -1, -1):
            commodity_after = self.commodities[i]
            current_indent = commodity_after.number_indents
            if commodity_after.number_indents > 1:
                for j in range(i - 1, -1, -1):
                    commodity_before = self.commodities[j]
                    if commodity_before.number_indents < current_indent:
                        commodity_after.hierarchy.append(commodity_before.description)
                        current_indent = commodity_before.number_indents

                    if commodity_before.number_indents == 1:
                        break
            commodity_after.hierarchy.append(commodity_after.heading_description)
            commodity_after.hierarchy.reverse()

        # for commodity in self.commodities:
        #     print(commodity.goods_nomenclature_item_id, str(commodity.number_indents))
    
    def as_dict(self):
        return {
            'id': self.goods_nomenclature_item_id,
            'description': self.description,
            "sub": self.hierarchy
        }
