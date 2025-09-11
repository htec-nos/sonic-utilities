import click
import utilities_common.cli as clicommon

##############################################################################
# ztest show commands
# show ztest hello-world
# ############################################################################

@click.group(cls=clicommon.AliasedGroup)
def ztest():
    """Show details of the test commands"""
    pass

@ztest.command()
def hello_world():
    """Show hello world"""
    click.echo("\nHello from SONiC CLI!\n")