# -*- coding: utf-8 -*-

"""Console script for hdgnetwork."""
import sys
import click
from .dns import Whois


@click.command()
@click.option(
        '-w',
        '--whois',
        type=click.STRING,
        help='Whois')
def main(whois):
    """Console script for hdgnetwork."""
    if whois:
        who = Whois()
        print(who.get_whois(whois))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
