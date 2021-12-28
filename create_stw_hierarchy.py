from classes.hierarchy_parser import HierarchyParser
import classes.globals


hierarchy_parser = HierarchyParser()
hierarchy_parser.build()
hierarchy_parser.write_hierarchy()