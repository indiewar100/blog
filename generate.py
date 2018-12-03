#!/usr/bin/python
# -*- coding:utf-8 -*-

import codecs

from markdown import Markdown


def markdown_to_html(self, file, file_type):
    with codecs.open(file, mode="r", encoding="utf-8", errors='ignore') as f:
        body = f.read()
        md = Markdown(extensions=['fenced_code', 'codehilite(css_class=highlight,linenums=None)',
                                  'meta', 'admonition', 'tables'])
        content = md.convert(body)
        meta = md.Meta if hasattr(md, 'Meta') else {}

        if file_type == 'post':
            data = self.parse_meta(file, meta)
            self.update_post_data(file, data)

            template = self.env.get_template('post.html')
            html = template.render(
                article=content,
                data=data,
                title=data.get('title')
            )
            return html
        elif file_type == 'page':
            url = meta['url'] or os.path.splitext(file)[0]
            meta['url'] = url
            self.update_page_data(file, meta)

            template = self.env.get_template('page.html')
            html = template.render(
                page=content,
                title=meta.get('title')[0] or os.path.splitext(file)[0]
            )
            return html