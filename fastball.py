# -*- coding: utf-8 -*-

import requests
import click


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
    print('Success! Link: ' + response.json()['link'])
    print('Your link expires in ' + response.json()['expiry'])


if __name__ == "__main__":
    fastball()

