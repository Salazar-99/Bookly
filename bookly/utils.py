from typing import List

def get_post_from_file(filepath: str) -> tuple:
    """
    Parses txt file for blog post contents and returns them
    """
    with open('test.txt', 'r') as f:
        raw = f.read()
        chunks = raw.split("\n")
        title = chunks[0].split(":")[1].strip()
        raw_tags = list(chunks[1].split(":")[1].split(","))
        tags = [tag.strip() for tag in raw_tags]
        raw_content = chunks[3:]
        content = ""
        for line in raw_content:
            content += line + " "
    return (title, tags, content)