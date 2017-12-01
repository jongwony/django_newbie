# Custom filter tags
# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
from django import template
from django.utils.encoding import force_text

import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang=None):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(mistune.escape(code))

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    _markdown = mistune.Markdown(renderer=renderer)
    return force_text(_markdown(value)).replace(r'<script>', r'&lt;script&gt;').replace(r'</script>', r'&lt;/script&gt;')
