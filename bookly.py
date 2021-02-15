import click
import click_repl
import os
from prompt_toolkit.history import FileHistory
from models import Post
from db import *
from utils import *
from errors import DuplicatePostError
from pymongo.errors import DuplicateKeyError

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
    post = Post.objects(title=title)[0]
    click.echo(post["title"])
    click.echo(post["content"])

@cli.command()
@click.option('--file')
def upload_post(file):
    click.echo("Parsing post file...")
    try:
        title, tags, content = get_post_from_file(file)
        post = Post(title=title, tags=tags, content=content)
    except:
        print("Problem parsing post file, check format")
    click.echo("Saving post...")
    if Post.objects(title=title).first() is None:
        post.save()
        click.echo("Post successfully uploaded!")
    else:
        print(f"Post with title '{title}' already exists")
    
@cli.command()
@click.option('--title')
def delete_post(title):
    click.echo("Looking for post...")
    try:
        post = Post.objects(title=title)
    except:
        click.echo("Post does not exist, try a different post title")
    click.echo("Deleting post...")
    try:
        post.delete()
    except:
        print(f"Failed to delete post with title: {title}")
    click.echo("Post successfully deleted!")