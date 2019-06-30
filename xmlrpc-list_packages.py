#! /usr/bin/env python3

"""
retourne la liste des packages
cf. https://warehouse.pypa.io/api-reference/xml-rpc/
"""

import xmlrpc.client
import json
import click
import logging
import sys


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-v", "--verbose", is_flag=True, default=False, help="verbose mode")
@click.option("--serial", is_flag=True, default=False, help="serial")
@click.option("--json", is_flag=True, default=False, help="json")
def main(**kwargs):

    # verbose/logger
    if sys.stdout.isatty():
        logging.addLevelName(logging.DEBUG, "\033[0;32m%s\033[0m" % logging.getLevelName(logging.DEBUG))
        logging.addLevelName(logging.INFO, "\033[1;36m%s\033[0m" % logging.getLevelName(logging.INFO))
        logging.addLevelName(logging.WARNING, "\033[1;33m%s\033[0m" % logging.getLevelName(logging.WARNING))
        logging.addLevelName(logging.ERROR, "\033[0;31m%s\033[0m" % logging.getLevelName(logging.ERROR))
        logging.addLevelName(logging.FATAL, "\033[1;41m%s\033[0m" % logging.getLevelName(logging.FATAL))

    if kwargs["verbose"]:
        logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S", level=logging.DEBUG)
        logging.debug("args %r", kwargs)
    else:
        logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S", level=logging.INFO)

    client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')

    if kwargs['serial']:
        packages = client.list_packages_with_serial()
    else:
        packages = client.list_packages()

    if kwargs['json']:
        print(json.dumps(packages, indent=2))
    else:
        for package in sorted(packages):
            print(package)


if __name__ == "__main__":
    main()
