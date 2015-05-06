#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: bcabezas@apsl.net

import click
import sys
from archiclean.importer import FileImporter
from archiclean.exporter import FileExporter
from archiclean.formatter import table_format


def cleaned_artifacts(importer, keep=2):
    """Yield artifacts with cleaned versions"""
    for artifact in importer:
        if artifact.has_number_and_year_releases:
            print("Warning: year and number based versions: \n")
        artifact.clean_releases(keep=keep)
        artifact.clean_snapshots(keep=keep)
        yield artifact


def artifact_tester(artifacts):
    """iter artifacts, and print warning if number and year mixed schema"""
    for artifact in artifacts:
        if artifact.has_number_and_year_releases:
            print("Warning: year and number based versions: \n")
        yield artifact


def clean_and_export_artifacts(importer, exporter, keep):
    for artifact in cleaned_artifacts(importer, keep=keep):
        exporter.export(artifact)


@click.group("archiclean")
def main():
    """exports archiva repository versions"""
    pass


@main.command()
@click.argument('from_path', type=click.Path(exists=True))
@click.argument('to_path', type=click.Path(exists=True))
@click.option('--keep', '-k', default=2, help='Number of versions to keep')
def export(from_path, to_path, keep):
    """Exports artifact releases and snapshots"""
    importer = FileImporter(from_path=from_path)
    exporter = FileExporter(to_path=to_path, from_path=from_path)
    clean_and_export_artifacts(importer, exporter, keep=keep)


@main.command()
@click.argument('from_path', type=click.Path(exists=True))
def list(from_path):
    """Lists artifact releases and snapshots"""
    importer = FileImporter(from_path=from_path)
    for artifact in artifact_tester(importer):
        print artifact


@main.command()
@click.argument('from_path', type=click.Path(exists=True))
@click.option('--cols', '-c', default=0, help='Column number (width) of table')
def list_warnings(from_path, cols):
    """Lists mixed artifact releases and snapshots"""
    importer = FileImporter(from_path=from_path)
    artifacts = (a for a in importer if a.has_number_and_year_releases)
    print table_format(artifacts, cols=cols)


if __name__ == '__main__':
    sys.exit(main())
