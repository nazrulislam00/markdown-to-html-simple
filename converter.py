def convert(markdown_text):
    html = markdown_text
    html = html.replace("### ", "<h3>") \
               .replace("## ", "<h2>") \
               .replace("# ", "<h1>")
    html = html.replace("\n", "<br>")
    return html

if __name__ == "__main__":
    with open("sample.md", "r") as md:
        markdown = md.read()

    html = convert(markdown)

    with open("output.html", "w") as out:
        out.write(html)

    print("Markdown converted to HTML")
