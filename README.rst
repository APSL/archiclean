==========
Archiclean
==========

Archiva repos cleaning and exporting tool.
This tool implements a version ordering oriented to solve a custom release problem: 
mixing *number-based* an *year-based* version naming schemes on artifacts.

usage:
------


* Exports artifact releases and snapshots FROM_PATH TO_PATH, keeping KEEP versions

    archiclean --keep=KEEP  FROM_PATH  TO_PATH

Will export separate repos TO_PATH/releases and TO_PATH/snapshots

* Lists artifact releases and snapshots

    archiclean list  FROM_PATH 

help: 
-----

    archiclean --help
    archiclean list --help
    archiclean export --help



Other info
----------

* Version cleaning stuff managed with python distutils.version
  * All ordering stuff here: https://github.com/APSL/archiclean/blob/master/archiclean/artifact.py#L46
* cmd management with http://click.pocoo.org/






