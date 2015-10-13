Annotation module
=================

Introductions
-------------
This module parse Illumina probe information and allows probe filtering, search and etc..

Contents
--------
Probe Class
^^^^^^^^^^^

.. class:: Probe()

    Creates a Probe object

    :rtype: Returns a probe object.


This object will hold all probe information. The following properties are currently supported.

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


ChrLoc Class
^^^^^^^^^^^^

.. class:: ChrLoc(chr, start, end)

   ChrLoc object holds genomic coordinates.

   :param chr: string
   :param start: integer
   :param end: integer
   :rtype: A ChrLoc object.

This object holds a chromosome interval used in genomics analysis.

USAGE:

.. code:: python

    my_probe = Annotation.ChrLoc("X", 122333232, 123334444)


Annotator Class
^^^^^^^^^^^^^^^

.. class:: Annotator()

    Creates an annotator object

    :rtype: Returns an annotation object.


This class *does* the majority of probe parsing work. It is required to have a **config.ini** in Data/ directory that point to the correct Illumina probe annotation dataset in CSV format. The data file can be downloaded from https://support.illumina.com/downloads.html .



USAGE:

.. code:: python

    annotations = Annotation.Annotator()


FUNCTIONS:


.. function:: get_probes_id_from_gene(gene_name)

    Get a list of probe ids associated with a gene.

    :param gene_name: Gene name string
    :return: A list of probe ids.

.. function:: get_probes_id_from_loc(probe_loc)

    Get all probes associated with genomic locations.

    :param probe_loc: Genomic Location.
    :return: a lst of probe ids.

.. function:: get_probes_id_from_cpg(cpg_loc)

    Get all probes associated with CpG sites.

    :param cpg_loc: CpG location
    :return: a lst of probe ids.

.. function:: get_probes_id_from_probe(probe_list)

    Get all probes ids from a list of probe objects.

    :param probe_list: A list of probe ids.
    :return: a list of probe ids.

.. function:: get_keys(dic_keys)

    Get Probe id from probe dictionaries

    :param dic_keys: Probe dict.
    :return: returns a list of probe id.

.. function:: get_probe(probe_id)

    This function returns the info associated with an id.

    :param probe_id: probe id
    :return: a probe object.

.. function:: get_probes(list_of_ids)

    This function returns the info associated with an id.

    :param list_of_ids: a probe id list
    :return: a list of probe objects.