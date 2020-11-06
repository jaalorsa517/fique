"""Script para agregar archivos al .gitignore"""

import click
import os


@click.command()
@click.argument("file", nargs=-1)
def main(file):
    '''Agrega ruta al archivo .gitignore'''
    with open(os.getcwd() + '/.gitignore','at') as f:
        for path in file:
            f.write(path+'\n')


if __name__ == "__main__":
    main()
