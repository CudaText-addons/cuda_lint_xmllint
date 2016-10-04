# Copyright (c) 2014 Aparajita Fishman
# License: MIT
# Change for CudaLint: Alexey T.

from cuda_lint import Linter, util


class Xmllint(Linter):
    """Provides an interface to xmllint."""

    syntax = 'XML'
    cmd = 'xmllint --noout * -'
    regex = (
        r'^.+?:'
        r'(?P<line>\d+):.+?: '
        r'(?P<message>[^\r\n]+)\r?\n'
        r'[^\r\n]+\r?\n'
        r'(?P<col>[^\^]*)\^'
    )
    multiline = True
    error_stream = util.STREAM_STDERR
