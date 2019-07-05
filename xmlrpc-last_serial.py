#! /usr/bin/env python3

import sys
import click
import xmlrpc.client


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--test", is_flag=True, default=False, help="test.pypi.org")
def main(test):

    if test:
        uri = "https://test.pypi.org/pypi"
    else:
        uri = "https://pypi.org/pypi"

    # https://warehouse.pypa.io/api-reference/xml-rpc/

    # server last_serial
    print(f"calling changelog_last_serial()")
    client = xmlrpc.client.ServerProxy(uri)
    last_serial = client.changelog_last_serial()
    print(f"server last_serial = {last_serial}")


if __name__ == "__main__":
    main()
