#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

import os
from functools import total_ordering
from datetime import datetime
from distutils.version import LooseVersion as V


@total_ordering
class FileArtifactVersion(object):
    """Artifact version directory management"""
    def __init__(self, basepath, name):
        self.basepath = basepath
        self.name = name

    def __repr__(self):
        id = 'S' if self.is_snapshot else 'R'
        return '{}({} / {})'.format(id, self.name, self.mtime.date())

    @property
    def is_snapshot(self):
        return 'SNAPSHOT' in self.name

    @property
    def is_release(self):
        return not self.is_snapshot

    @property
    def path(self):
        return os.path.join(self.basepath, self.name)

    @property
    def mtime(self):
        return datetime.fromtimestamp(os.stat(self.path).st_mtime)

    @property
    def path(self):
        return os.path.join(self.basepath, self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        """Consideramos mayor o menor segun nombre de version"""
        if V(self.name) > V(other.name) and self.mtime.date() < other.mtime.date():
            print "WARN:{} {} {} / {} {} {}".format(
                    self.basepath, self.name, self.mtime, other.basepath, other.name, other.mtime)
            #import ipdb;ipdb.set_trace()
        return V(self.name) > V(other.name)

    @staticmethod
    def is_valid_version(version):
        """True if version begins with digit"""
        return version[0].isdigit()


class FileArtifact(object):
    """Artifact file backend"""
    def __init__(self, path, versions):
        self.path = path
        versions = [FileArtifactVersion(path, v) for v in versions
                if FileArtifactVersion.is_valid_version(v)]
        self._snapshots = sorted([v for v in versions if v.is_snapshot])
        self._releases = sorted([v for v in versions if v.is_release])

    @property
    def id(self):
        return os.path.basename(self.path)

    @property
    def releases(self):
        return self._releases

    @property
    def snapshots(self):
        return self._snapshots

    def __repr__(self):
        return 'Artifact ({})'.format(self.path)

    def __str__(self):
        return 'Artifact ({})\n  |-releas-> * {}\n  |-snaps--> * {}'.format(
                self.path,
                '\n             * '.join(str(v) for v in self.releases),
                '\n             * '.join(str(v) for v in self.snapshots)
        )

    def clean_releases(self, keep=2):
        self._releases = self._releases[-keep:]

    def clean_snapshots(self, keep=2):
        self._snapshots = self._snapshots[-keep:]

    @classmethod
    def from_path(cls, path, dirnames=[], filenames=[]):
        """Factory from directory path
        @returns artifact, or None if no artifact for this path
        """

        if dirnames and 'maven-metadata.xml' in filenames:
            return cls(path=path, versions=dirnames)
