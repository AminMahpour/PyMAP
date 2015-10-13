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

- *probe id:* a **string** is Illumina probe id.
- *seq:* a **string** holds the sequence associated with the probe.
- *name:* a **string** that holds probe name.
- *chr:* a **string** holds chromosome number.
- *cord:* an **integer** holds the coordinate of probe.
- *strand:* a **string** holds probe strand. either F or R.
- *gene:* a **string** that holds Associated gene.
- *refseq:* a **string** holds refseq info.

* Create a new probe object:

.. code:: python

    my_probe = Probe()


ChrLoc
^^^^^^
This object holds a chromosome interval used in genomics analysis.


.. class:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings

Annotator Class
^^^^^^^^^^^^^^^
This class *does* the majority of probe parsing work. It is required to have a **config.ini** in Data/ directory that point to the correct Illumina probe annotation dataset in CSV format. The data file can be downloaded from https://support.illumina.com/downloads.html .
