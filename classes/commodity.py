import sys
import classes.globals as g


class Commodity(object):
    def __init__(self, attributes, heading_description):
        self.goods_nomenclature_item_id = attributes["goods_nomenclature_item_id"]
        self.productline_suffix = attributes["producline_suffix"]
        self.code = self.goods_nomenclature_item_id + "_" + self.productline_suffix
        self.description = attributes["formatted_description"]
        if self.description == "":
            self.description = g.app.eu_commodities[self.code]
            print(self.goods_nomenclature_item_id, "has no description, using EU equivalent instead")
            # sys.exit()
        self.cleanse_description()
        self.declarable = attributes["leaf"]
        self.number_indents = attributes["number_indents"]
        self.heading_description = heading_description
        self.hierarchy = []
        
    def cleanse_description(self):
        self.description = self.description.replace("\u00a0", "&nbsp;")
        self.description = self.description.replace("\u00e9", "&eacute;")
        self.description = self.description.replace("|", " ")
    
    def as_dict(self):
        return {
            'id': self.goods_nomenclature_item_id,
            'description': self.description,
            "sub": self.hierarchy
        }
