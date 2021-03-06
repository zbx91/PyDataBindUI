# -*- coding: utf-8 -*-
import importlib
import xml.etree.ElementTree as ET
from internal.prop_watcher  import PropWatcher
# class XMLParser(object):
#     def get_class(fullname):
#         i = fullname.rfind('.')
#         pkgname, modname = fullname[:i], fullname[i + 1:]
#         mod = importlib.import_module(pkgname)
#         cls_name = mod.__dict__[modname]
#         return cls_name


#     def parse_xml(ui, xml_name):
#         tree = ET.parse(xml_name)
#         root = tree.getroot()
        
#         # context
#         context_fullname = root.attrib.get('name')
#         setattr(ui, 'model', get_class(context_fullname)())

#         for node in root:
#             node_type = node.attrib.get('type')
#             if node_type == 'node':
#                 view_name = node.find('name').text
#                 print 'view_name', view_name
#                 view = get_class(view_name)()


def get_class(fullname):
    i = fullname.rfind('.')
    pkgname, modname = fullname[:i], fullname[i + 1:]
    mod = importlib.import_module(pkgname)
    cls_name = mod.__dict__[modname]
    return cls_name




def parse_xml(ui, xml_name):
    tree = ET.parse(xml_name)
    root = tree.getroot()
    
    # context
    context_fullname = root.attrib.get('name')
    setattr(ui, 'model', get_class(context_fullname)())

    for node in root:
        node_type = node.attrib.get('type')
        node_name = node.attrib.get('name')
        if node_type == 'node':

            ui_node = ui.get_node('node_name')
            
            for data_bind in node.findall('data-bind'):
                view = get_class(data_bind.find('view').find('name').text)(ui_node)
                view_attr = data_bind.find('view').find('attr').text
                vmodel = ui.model
                vmodel_attr = data_bind.find('view-model').find('attr').text
                PropWatcher(view, view_attr, vmodel, vmodel_attr)
                

                



        elif node_type == 'animation':
            pass