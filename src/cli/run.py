import click
from lib.config import Config
from lib.sync.unison import UnisonDaemon
from lib.ssh import SSH


@click.group()
def cli():
    pass


@cli.command()
@click.option("--domain", required=True)
@click.option("--connect", is_flag=True,
              help="Auto connect after setting config")
def config(domain, connect):
    """This command makes the Nvie Config"""
    c = Config(domain)
    c.initialise_config()
    click.echo("Container Created")


@cli.command()
def connect():
    """This command conects to the Nvie compute instance"""
    c = Config.load_config()
    u = UnisonDaemon(c.domain, c.host)
    click.echo(
        "Syncing current directory to {0} directory {1}"
        .format(u.host, u.server_folder)
    )
    pid = u.start()
    click.echo(
        "Connection to remote machine...."
    )
    s = SSH(c.host, c.container_id)
    s.connect()
    input("Press any key to stop sync.")
    pid.kill()
