# -*- coding: utf-8 -*-

"""Console script for hdgnetwork."""
import ipaddress
import sys

# 3rd party libraries
import click

from . import __version__
from .whois import Whois


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'hdg %(version)s (Python {})'
    return message.format(python_version)


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(
        __version__,
        '-V',
        '--version',
        message=version_msg(),
        help='Output the version of the application')


@click.pass_context
def main(ctx):
    """HDG is a network tool suite

    Here a better description
    """
    pass


@main.command('whois')
@click.argument('data', nargs=1)
@click.pass_context
def whois(ctx, data):
    """Perform a whois request on a domain or IP

    IPv4 and IPv6 are accepted.

    Examples:\n
        hdg whois 93.184.216.34\n
        hdg whois example.net\n
        hdg whois 2606:2800:220:1:248:1893:25c8:1946\n
    """
    whois = Whois()
    try:
        ipaddress.ip_address(data)
        # data is an IP v4 or v6 address
        result = whois.get_from_ip(data)
        print(result)
    except ValueError:
        # data is a domain
        click.echo('It is a domain')


if __name__ == "__main__":
    cli()  # pragma: no cover
