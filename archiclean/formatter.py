#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

from texttable import Texttable
from os.path import basename, dirname


def table_format(artifacts):
    """Formats an artifact"""
    table = Texttable(max_width=0)
    table.header(['Group (dir)', 'Artifact', 'Releases', '', 'Snapshots', ''])
    #table.set_cols_align(["l", "l", "l", "l"])
    #table.set_cols_valign(["t", "t", "t", "t"])
    for artifact in artifacts:
        table.add_row([
            dirname(artifact.name),
            basename(artifact.name),
            "\n".join([v.name for v in artifact.releases]),
            "\n".join(["{}".format(v.mtime.date()) for v in artifact.releases]),
            "\n".join([v.name for v in artifact.snapshots]),
            "\n".join(["{}".format(v.mtime.date()) for v in artifact.snapshots]),
            ])
    return table.draw()
