#!/usr/bin/env python

import json
import os

import yaml


class Loader(yaml.SafeLoader):
    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, "r") as f:
            return yaml.load(f, Loader)


Loader.add_constructor("!include", Loader.include)

with open("example.yaml", "r") as stream:
    try:
        data = yaml.load_all(stream, Loader=Loader)
        for d in data:
            print(json.dumps(d, indent=2))
    except yaml.YAMLError as exc:
        print(exc)
