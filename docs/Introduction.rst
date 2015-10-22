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

In the first example, we will create an annotation object that you can use to extract methylation values form samples. This object will hold Illumina probe information.

..  code-block:: python
    :linenos:

    # Import Annotation submodule to parse and prepare probe information.
    import pymap.Annotation

    # Create Annotation object. This object well parse through all probes annotation information Illumina has provided for probes used in 450K platform.
    annotation = pymap.Annotation.Annotator()

    # Get number of probes in the annotation object.
    probe_number = annotation.get_number()
    print(probe_number)

    # Remove known SNPs easily with a simple method. This filteration step might be useful for most studies in human subjects.
    annotation.remove_snp_probes()

    # Get number of probes after SNP removal from the annotation object.
    probe_number = annotation.get_number()
    print(probe_number)

In the second example, we parse samples:

..  code-block:: python
    :linenos:

    # Import Core submodule to parse data.
    import pymap.Core

    # Parse a single data file.
    parsed_samples = Core.ParseFile("data.txt")

    # Parse multiple data file.
    parsed_samples = Core.ParseBatch("/Data")

    # Get Sample data from either one or multiple files. samples contains a list of samples. Please see sample object documentations.
    samples = parsed_samples.get_samples()

In the third example, we integrate Core and Annotation objects to extract methylation data from p53 gene probes:

..  code-block:: python
    :linenos:

    # Get all probes associated with p53 gene:
    probe_list = annotations.get_probes_from_gene("TP53")

    # Export data associated with selected probes and samples into a data frame:
    pymap.Core.write_data("data.txt", samples, probe_list)

    # Export probe and methylation data into BED file format.
    # In this example we export data for the first sample (sample[0]).
    pymap.Core.probes_to_bed("Export/test2.bed", probe_list, samples[0])

    # Export all samples into separate BED file.
    pymap.Core.samples_to_bed("Export/me", probe_list, samples)


Citation and Contact
--------------------
Please cite this package with the Github URL until it is published. Please contact authors using Gitub platform for any inquiry.
