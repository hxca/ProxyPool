# -*- coding:utf-8 -*-


import click
import WebApi
import ProxyScheduler


def cli():
    pass


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='2.0.0')
def cli():
    """ProxyPool cli工具"""


@cli.command(name="schedule")
def schedule():
    ProxyScheduler.run_scheduler()


@cli.command(name="webserver")
def schedule():
    WebApi.run_flask()


if __name__ == '__main__':
    cli()
