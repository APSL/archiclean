#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

#from sh import rsync
from os.path import join, relpath
from os import makedirs
from shutil import copytree


class FileExporter:
    """Exporta artifact"""
    def __init__(self, to_path, from_path):
        self.to_path = to_path
        self.from_path = from_path

    def export(self, artifact):
        """Exporta artifact"""
        rel = relpath(artifact.path, self.from_path)
        self._export_versions(
                dst=join(self.to_path, 'releases',  rel),
                versions=artifact.releases)
        self._export_versions(
                dst=join(self.to_path, 'snapshots',  rel),
                versions=artifact.snapshots)
        print artifact

    def _export_versions(self, dst, versions):

        makedirs(dst)

        for version in versions:
            src = version.path
            dst = join(dst, version.name)
            copytree(src, dst)
