index_html = './templates/index.html'
with open(index_html, 'r') as file:
    lines = file.readlines()
    modified_lines = [];
    for line in lines:
        if 'src="' in line and 'static/' not in line:
            line = line.replace('src="', 'src="static/')
        if 'favicon' in line and 'static' not in line:
            line = line.replace('href="favicon.ico"', 'href="static/favicon.ico"')
        modified_lines.append(line)
    html_content = "".join(modified_lines)
    print(html_content)
    with open(index_html, 'w') as file_write:
        file_write.write(html_content)
