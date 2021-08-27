# -*- coding: utf-8 -*-
import os
import markdown
from bs4 import BeautifulSoup


def header_text(site_name: str) -> str:
    return '''
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta name="robots" content="noindex">
    <script type="text/javascript" src="../../contents_builder.js"></script>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <!-- StyleSheet -->
    <style>
        @import "../../stylesheets/grid.css";
        @import "../../stylesheets/header.css";
        @import "../../stylesheets/footer.css";
        @import "../../stylesheets/h2icon.css";
        @import "../../stylesheets/page_elements.css";
        @import "../../stylesheets/linkbutton_grid.css";
        @import "../../stylesheets/media.css";

        body {
            margin: 0;
            background: #f9fff6;
            text-align: center;
        }

        h3 {
            margin-top: 2em;
        }

        #main_wrapper {
            max-width: 1000px;
        }

        h2.trpfrog::before {
            background-image: none;
            width: 0;
            margin-right: 0;
        }

        p.images {
            text-align: center;
        }

        img {
            max-width: 90%;
        }

        h2::before {
            background-image: none !important;
            width: 0 !important;
            margin-right: 0 !important;
        }
    </style>
    <!---------------->
    <meta charset="utf-8">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@TrpFrog">
    <meta property="og:url" content="https://www.trpfrog.net">
    <meta property="og:title" content="つまみネット">
    <meta property="og:description" content="さかなになりたいね">
    <meta property="og:image" content="https://www.trpfrog.net/images/TwitterCard.png">
    <title>''' + site_name + ''' - つまみネット</title>
</head>
    '''

def content_text(title: str, description: str, content_HTML: str) -> str:
    return '''
    <body>
        <div class="grid">
            <header></header>
            <main>
                <div id="main_wrapper">
                    <div id="title">
                        <h1>''' + title + '''</h1>
                        <p>
                            ''' + description + '''
                        </p>
                    </div>
                    <div class="main_window">
                        ''' + content_HTML + '''
                    </div>
                </div>
            </main>
            <footer></footer>
        </div>
    </body>
</html>'''


def make_toppage():
    with open('index.html', 'w') as f:
        f.write(header_text('雑記'))
        # f.write(content_text('Random Notes',
        #                      'ブログに書くほどでもない記事とか'))

def make_blogpage(md: markdown.Markdown, file_name: str):
    button = '<a href="../index.html" class="linkButton" style="margin: 5px">記事一覧</a>'
    with open(f'{file_name}/index.html', 'w') as f:
        with open(f'{file_name}/{file_name}.md', 'r') as f_md:
            html = md.convert(f_md.read())
            soup = BeautifulSoup(html, "html.parser")
            title = soup.find('h1').text
            html = '\n'.join(html.split('\n')[1:])
            f.write(header_text(f'雑記「{title}」'))
            f.write(content_text(title, button, html))

if __name__ == '__main__':
    folders = os.listdir('.')
    md = markdown.Markdown()
    make_toppage()
    for folder in folders:
        if os.path.isfile(folder):
            continue
        make_blogpage(md, folder)