# -*- coding: utf-8 -*-

import requests
import click
import pyperclip

@click.command()
@click.option('--e', '--expires', default='1w', type=str, help='Set expiry of link: 1w = 1 week, 2d = 2 days, 3m = 3 months, etc.')
@click.argument('f', type=click.Path(exists=True))

def fastball(e, f):
    params = (
        ('expires', e),
    )

    files = {
        'file': (str(click.format_filename(f)), open(f, 'rb'))
    }

    response = requests.post('https://file.io/', params=params, files=files)
    click.echo(click.style('Success! ', fg="green", bold=True), nl=False)
    click.echo('    ' + response.json()['link'])
    click.echo(click.style('Expires in:  ', fg="red", bold=True), nl=False)
    click.echo(response.json()['expiry'])
    
    pyperclip.copy(response.json()['link'])
    click.echo(click.style('--> Your link has been copied to the clipboard.', bold=True))


if __name__ == "__main__":
    fastball()

