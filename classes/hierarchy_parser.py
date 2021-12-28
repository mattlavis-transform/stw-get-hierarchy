import requests
import os
import json
from dotenv import load_dotenv

from classes.chapter import Chapter


class HierarchyParser(object):
    def __init__(self):
        load_dotenv('.env')
        self.root_url = os.getenv('ROOT_URL')
        self.date = os.getenv('DATE')
        if self.date == "":
            self.date_param = ""
        else:
            self.date_param = "?as_of=" + self.date
            
        self.chapters = []
        self.codes = []

    def build(self):
        min = 1
        max = 99
        for i in range(min, max + 1):
            if i != 77:
                url = self.root_url + "chapters/" + str(i).zfill(2) + self.date_param
                response = requests.get(url)
                if response:
                    json = response.json()
                    data = json["data"]
                    included = json["included"]
                    chapter = Chapter(data["attributes"], included, self.date_param)
                    self.chapters.append(chapter)

    def write_hierarchy(self):
        for chapter in self.chapters:
            for heading in chapter.headings:
                if heading.declarable:
                    self.codes.append(heading.as_dict())
                else:
                    for commodity in heading.commodities:
                        if commodity.declarable:
                            self.codes.append(commodity.as_dict())

        path = os.getcwd()
        path = os.path.join(path, "output", "codes.json")
        with open(path, "w") as outfile:
            json.dump(self.codes, outfile, indent = 4)