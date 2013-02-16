===========
unicode_csv
===========

Python2k's csv module doesn't support Unicode input. This is described in the
document. (cf. `csv`_)

.. _`csv`: http://docs.python.org/2.7/library/csv.html

To read Unicode input, you should write wrapper and re-code the encoding. For
instance, if you want to read a file encoded in cp932, you should do cp932 ->
unicode -> utf8 -> csv -> utf8 -> unicode conversion. The `csvwrapper`_
library will do this conversion for you.

.. _`csvwrapper`: https://github.com/draftcode/csvwrapper

Although the csvwrapper library reads any file properly, the reading speed is
much decreased. (10 times slower in my PC)

This module aims to port Python3k's csv module, which supports Unicode input,
to Python2k.

