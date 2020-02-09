Linter for CudaLint plugin.
It adds support for XML lexer.

Linux
-----
Install package "libxml2".

Windows
-------
It is not necessary to install Cygwin to be able to use the XML linter because (as the xmlsoft site states) there are native Windows binaries available at this site:
https://www.zlatkovic.com/projects/libxml/index.html

I was able to get the XML linter running by downloading the following packages, they are available via the download area of the site mentioned above:

    libxml2 (download libxml2-2.7.8.win32.zip)
    iconv (download iconv-1.9.2.win32.zip)
    zlib (download zlib-1.2.5.win32.zip)

After unpacking the ZIP packages, one has to navigate into the "bin" folder contained in every package and copy the following files into a single directory:

    xmllint.exe
    libxml2.dll
    iconv.dll
    zlib1.dll

This directory has to be added to the PATH variable.


Author: Alexey Torgashin (CudaText)
License: MIT
