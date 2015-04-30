#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

import os
from archiclean.artifact import FileArtifact


class FileImporter:
    """Importa artifacts de un directorio"""
    def __init__(self, from_path):
        self.from_path = from_path

    def __iter__(self):
        """Iterador de artifacfs"""
        for parentdir, dirnames, filenames in os.walk(self.from_path):
            artifact = FileArtifact.from_path(parentdir, dirnames, filenames)
            if artifact:
                yield artifact
            #if FileArtifact.path_is_artifact(path=parentdir, dirnames, filenames):
                #yield FileArtifact(path=parentdir, versions=dirnames)
