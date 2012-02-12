Python Audio Tools (proof of concept)
=====================================

Proof of concept projecto to test some audio encodings using Python and Audio
Tools.


Requisites
----------
::

- python > 2.5
- gcc compiler
- libcdio libcdio-dev
- libcdio-cdda0 libcdio-cdda-dev
- libcdio-paranoia0 libcdio-paranoia-dev 
- lame or mpg123 for mp3 conversion
- faad and faac for M4A decoding and encoding.

Installation
------------

Installed version 2.17 from github on a virtualenv using pip.
The installation complains about not being able to copy 'audiotools.cfg' to /etc
but the library is correctly installed on my virtualenv.


