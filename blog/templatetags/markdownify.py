# Custom filter tags
# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
from django import template
import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(mistune.escape(code))

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter(is_safe=True)
def markdown(value):
    _markdown = mistune.Markdown()
    return _markdown(value)
