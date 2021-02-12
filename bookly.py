import click
import click_repl
import os
from prompt_toolkit.history import FileHistory
from models import Post
from db import *
from utils import *

configure_and_connect()

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Bookly CLI
    """
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)

@cli.command()
def repl():
    """
    Start an interactive session
    """
    prompt_kwargs = {
        'history': FileHistory(os.path.expanduser('~/.repl_history'))
    }
    click_repl.repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)

@cli.command()
@click.option('--name', default='world')
def hello(name):
    """Say hello"""
    click.echo('Hello, {}!'.format(name))

@cli.command()
def get_posts():
    """
    Retrieve and display all blog posts
    """
    for post in Post.objects:
        click.echo("\n")
        click.echo(post["title"])
        click.echo(post["content"])
        click.echo("\n")

@cli.command()
@click.option('--title')
def get_post_by_title(title):
    """
    Retrieve and display post with the given title if it exists
    """
    #TODO: Add validation for empty response
    post = Post.objects(title=title)[0]
    click.echo("\n")
    click.echo(post["title"])
    click.echo(post["content"])
    click.echo("\n")

@cli.command()
@click.option('--file')
def add_post(file):
    title, tags, content = get_post_from_file(file)
    post = Post(title=title, tags=tags, content=content)
    post.save()
    click.echo("Post successfully uploaded")

@cli.command()
@click.option('--file')
def update_post(file):
    #Delete old post
    #add new post