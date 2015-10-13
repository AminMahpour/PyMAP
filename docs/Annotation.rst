Annotation module
=================

Introductions
-------------
This module parse Illumina probe information and allows probe filtering, search and etc..

Contents
--------
Probe Class
^^^^^^^^^^^
This object will hold all probe information. The following information is currently supported.

- *probe id:* This is Illumina probe id.

Annotator Class
^^^^^^^^^^^^^^^
This class *does* the majority of probe parsing work. It is required to have a **config.ini** in Data/ directory that point to the correct Illumina probe annotation dataset in CSV format. The data file can be downloaded from https://support.illumina.com/downloads.html .

.. autoclass:: Annotation
