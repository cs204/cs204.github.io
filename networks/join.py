#!/usr/bin/env python3
# Из файлов шаблонов в templates
# собираются странички и сохраняются в root 
# вспомогательная папка static в неё все кроме html

from jinja2 import Environment, FileSystemLoader
import os

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
static_dir = os.path.join(root, 'static')
env = Environment(loader = FileSystemLoader([templates_dir, static_dir]))

file_names = os.listdir(templates_dir)
for file in file_names:
    template = env.get_template(file) 
    filename = os.path.join(root,  file) 
    with open(filename, 'w') as fh: 
        fh.write(template.render())
