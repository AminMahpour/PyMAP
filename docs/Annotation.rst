Annotation module
=================

Introductions
-------------
This module parse Illumina probe information and allows probe filtering, search and etc..

Contents
--------
Probe Class
^^^^^^^^^^^
This object will hold all probe information. The following proterties are currently supported.

- *probe id:* a **string** is Illumina probe id.
- *seq:* a **string** holds the sequence associated with the probe.
- *name:* a **string** that holds probe name.
- *chr:* a **string** holds chromosome number.
- *cord:* an **integer** holds the coordinate of probe.
- *strand:* a **string** holds probe strand. either F or R.
- *gene:* a **string** that holds Associated gene.
- *refseq:* a **string** holds refseq info.


USAGE:

.. code:: python

    my_probe = Annotation.Probe()


ChrLoc
^^^^^^

.. class:: ChrLoc(chr, start, end)

   ChrLoc object holds genomic coordinates.

   :param chr: string
   :param start: integer
   :param end: integer
   :rtype: A ChrLoc object.

This object holds a chromosome interval used in genomics analysis.


Annotator Class
^^^^^^^^^^^^^^^

.. class:: Annotator()

    Creates an annotator object

    :rtype: Returns an annotation object.


This class *does* the majority of probe parsing work. It is required to have a **config.ini** in Data/ directory that point to the correct Illumina probe annotation dataset in CSV format. The data file can be downloaded from https://support.illumina.com/downloads.html .



USAGE:

.. code:: python

    annotations = Annotation.Annotator()

