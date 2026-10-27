"""Pygments lexer for Kleio notation.

Kleio is the source-transcription notation of the Timelink system for
historical research (https://github.com/time-link). Ported from the
TextMate grammar in time-link/kleio-grammar (scope ``source.kleio``)
and from the prism-kleio grammar, with two fixes: correct ``A-Za-z``
character ranges (the originals had ``A-z``) and underscores allowed
in group/element names (e.g. ``/place_of_burial=``).
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Name,
    Number,
    Punctuation,
    String,
    Text,
    Whitespace,
)

__all__ = ["KleioLexer"]


class KleioLexer(RegexLexer):
    """Lexer for Kleio notation and Timelink translation reports."""

    name = "Kleio"
    aliases = ["kleio", "cli"]
    filenames = ["*.kleio", "*.cli", "*.rpt"]
    url = "https://github.com/time-link/kleio-grammar"

    tokens = {
        "root": [
            # translation-report errors and warnings (.rpt output)
            (r"^ERROR:.*$", Error),
            (r"^[0-9]*\s\serrors\.$", Error),
            (r"^WARNING:.*$", Generic.Deleted),
            (r"^[0-9]*\s\swarnings\.$", Generic.Deleted),
            # '**' comment lines
            (r"^\*\*\s.*$", Comment.Preproc),
            # report line numbers:  "12: n$jose/..."
            (r"^[0-9]+:", Number),
            # group with positional core:  "n$filipa/f"
            # (fixed A-z range; core runs to the first separator)
            (r"^([ \t]*)([a-z_][a-z0-9_.-]*)(\$)([A-Za-z0-9 .-]*)",
             bygroups(Whitespace, Name.Class, Punctuation, Name.Function)),
            # group without core:  "fonte$xpto"
            (r"^([ \t]*)([a-z_][a-z0-9_.-]*)(\$)",
             bygroups(Whitespace, Name.Class, Punctuation)),
            # identification elements, with their value
            (r"(/)(id|mesmo_que|xmesmo_que|same_as|xsame_as)(=)([A-Za-z0-9.-]*)",
             bygroups(Punctuation, Keyword.Type, Punctuation, Name.Variable)),
            # named elements:  /obs=... /tipo=... /place_of_burial=...
            # (underscores allowed, unlike the source grammars)
            (r"(/)([a-z_][a-z0-9_.-]*)(=)",
             bygroups(Punctuation, Keyword, Punctuation)),
            # original source reading:  %lousa vila
            (r"(%)([^/\n]*)", bygroups(Punctuation, Comment.Special)),
            # transcriber note:  #cargo: padre
            (r"(#)([^%\n]*)", bygroups(Punctuation, Comment.Single)),
            # double-quoted strings
            (r'"[^"]*"', String.Double),
            # separators
            (r"[/=$]", Punctuation),
            (r"\n", Whitespace),
            (r".", Text),
        ]
    }
