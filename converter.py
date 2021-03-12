#!/usr/bin/python
import pyheif
from PIL import Image
import click
import pathlib
import os

welcome = """

████████  █████  ██       █████  ██      ███████ 
   ██    ██   ██ ██      ██   ██ ██      ██      
   ██    ███████ ██      ███████ ██      ███████ 
   ██    ██   ██ ██      ██   ██ ██           ██ 
   ██    ██   ██ ███████ ██   ██ ███████ ███████ 
                                                 

██   ██ ███████ ██  ██████     ████████  ██████           ██ ██████  ███████ ███████ 
██   ██ ██      ██ ██             ██    ██    ██          ██ ██   ██ ██      ██      
███████ █████   ██ ██             ██    ██    ██          ██ ██████  █████   █████ 
██   ██ ██      ██ ██             ██    ██    ██     ██   ██ ██      ██      ██    
██   ██ ███████ ██  ██████        ██     ██████       █████  ██      ███████ ██ 
                                                                                

 ██████  ██████  ███    ██ ██    ██ ███████ ██████  ████████ ███████ ██████ 
██      ██    ██ ████   ██ ██    ██ ██      ██   ██    ██    ██      ██   ██ 
██      ██    ██ ██ ██  ██ ██    ██ █████   ██████     ██    █████   ██████  
██      ██    ██ ██  ██ ██  ██  ██  ██      ██   ██    ██    ██      ██   ██ 
 ██████  ██████  ██   ████   ████   ███████ ██   ██    ██    ███████ ██   ██ 
                                                                             

"""

def heic_to_jpeg(source_folder, file, target_folder):
    with open(f'{source_folder}/{file}', 'rb') as f:
        data = f.read()
        i = pyheif.read_heif(data)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        new_image = target_folder + "/" + file.split('.')[0] + ".jpg"
        pi.save(new_image, format="jpeg")
        click.echo(f'Saved {f.name} as {new_image}')

@click.group()
def cli():
    click.echo(welcome)
    pass

@cli.command()
@click.option('-t', '--target-folder', type=str, help='Folder to write converted images to', default='./converted')
@click.option('-s', '--source-folder', type=str, help='Folder to read HEIC images from', default='.')
@click.option('-l', '--list-only', type=bool, help='Only list the files that will be converted but don\'t convert yet', flag_value=True, default=False)
def convert(target_folder, source_folder, list_only):
    click.echo("\n=============================================")
    click.echo(f'Converting all files in  "{source_folder}" and writing to "{target_folder}"')
    click.echo("\n=============================================")
    pathlib.Path(target_folder).mkdir(parents=True, exist_ok=True)
    files = [f for f in os.listdir(source_folder) if os.path.isfile(f'{source_folder}/{f}') and os.path.splitext(f)[1][1:].strip().lower() == "heic" ]
    click.echo(f'Files to convert:')
    for file in files:
        click.echo(f'           --- {file}')
    click.echo("\n=============================================")
    if list_only:
        return
    for file in files:
        heic_to_jpeg(source_folder, file, target_folder)
    click.echo("\n=============================================")
    click.echo("Done!\n")
