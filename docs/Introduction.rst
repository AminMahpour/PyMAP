Introduction
============

Why pyMAP?
----------
This is a very interesting question that desevered to be answered properly. All 450K platform analysis software developed so far are made using R.
While we think R is a power statistical platform, we also believe in diversity of analysis platforms. Python, which is a powerful language can also be used for these analysis.
pyMAP, implemented in native python, offers a more powerful alternative which utilizes python scripts and can also be modified further.

Documentation
-------------

Here we have provided detailed documentation on Classes and Functions in this module.

Examples
--------
Here goes an example of what pymap can do!

..  code-block:: python
    :linenos:

    # Create Annotation object. This object well parse through all probes annotation information Illumina has provided for probes used in 450K platform.
    annotation = pymap.Annotation.Annotator()

    # Get number of probes in the annotation object.
    probe_number = annotation.get_number()

    # Remove known SNPs easily. This filteration might be useful for most studies in human subjects.
    SNP_filtered = annotation.remove_SNP_probes()


Citation and Contact
--------------------
Please cite this package with the Github URL until it is published. Please contact authors using Gitub platform.
