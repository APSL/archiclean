#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

import click
import sys
from archiclean.importer import FileImporter
from archiclean.exporter import FileExporter


def cleaned_artifacts(importer, keep=2):
    """Yield artifacts with cleaned versions"""
    for artifact in importer:
        artifact.clean_releases(keep=keep)
        artifact.clean_snapshots(keep=keep)
        yield artifact


def clean_and_export_artifacts(importer, exporter, keep):
    for artifact in cleaned_artifacts(importer, keep=keep):
        exporter.export(artifact)


@click.command()
@click.argument('from_path', type=click.Path(exists=True))
@click.argument('to_path', type=click.Path(exists=True))
@click.option('--keep', '-k', default=2, help='Number of versions to keep')
def main(from_path, to_path, keep):
    importer = FileImporter(from_path=from_path)
    exporter = FileExporter(to_path=to_path, from_path=from_path)
    clean_and_export_artifacts(importer, exporter, keep=keep)


if __name__ == '__main__':
    sys.exit(main())
