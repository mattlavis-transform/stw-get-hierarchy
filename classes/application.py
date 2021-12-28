import os
from dotenv import load_dotenv

from classes.database import Database


class Application(object):
    def __init__(self):
        self.get_environment_variables()
        self.get_eu_commodities()
        
    def get_environment_variables(self):
        load_dotenv('.env')
        self.root_url = os.getenv('ROOT_URL')
        self.date = os.getenv('DATE')
        if self.date == "":
            self.date_param = ""
        else:
            self.date_param = "?as_of=" + self.date
        
    def get_eu_commodities(self):
        self.eu_commodities = {}
        for i in range(0, 10):
        # for i in range(0, 10):
            chapter = str(i) + "%"
            sql = """select goods_nomenclature_item_id, producline_suffix,
            description from utils.goods_nomenclature_export_new(%s, %s) order by 1, 2"""
            
            print("Getting EU codes beginning with " + str(i))
            d = Database()
            params = [
                chapter,
                self.date
            ]
            rows = d.run_query(sql, params)
            for row in rows:
                code = row[0] + "_" + row[1]
                self.eu_commodities[code] = row[2]
            a = 1
