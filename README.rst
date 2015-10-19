
PYMAP PYTHON PACKAGE TO ANALYZE 450K METHYLATION DATA.
======================================================
PyMAP is a python package for efficient and fast analyzing of Illumina 450K methylation data.


Example pipeline:
-----------------
    #load submodules

    import Annotation
    import Core
    import Plot

    #Load probe annotations
    #Make sure config.ini is set to correct Illumina probe dataset.

    annotations = Annotation.Annotator()

    #load and parse a single methylation file that might contain info for one or more sample.

    methyl_file = "EXAMPLE.txt"
    samples = Core.ParseFile(methyl_file).get_sample()

    #load and parse multiple methylation files

    methyl_directory = "Data/"
    samples = Core.ParseBatch(methyl_directory).get_all_samples()

    #get probes associated with a gene

    gene= "TP53"
    probe_list = annotations.get_probes_from_gene(gene)
    print(probe_list)

    #get sample name and beta values from parse data

    for sample in samples:
        print(sample.name)
        beta_values = sample.probes  # beta_values are loaded from each sample.

    #plot probes that are assciated with p53 gene and save it as PNG image file.

    Plot.Heatmap(samples, probe_list, "p53_methylation.png")


COMMAND LINE EXECUTABLES:
-------------------------

convertbed.py creates a BED file that contains all information about probes that are associated with a specified gene.

    USAGE:
         ./convertbed.py -file Data/METHYL_DATA.txt -out TP53.bed -gene TP53




getidfromgene.py generates a text file that contains probe ids associated with a gene

    USAGE:
        ./getidfromgene.py -gene TP53 -out y



samplebed.py create multiple BED files that each represent a sample. the gene is also need to be specified.

    USAGE:
        ./samplebed.py -file Data/GSE42308.txt -out Export/TP53 -gene TP53



PlotProbe.py generates heatmap plot of probes that are associated with a gene.

    USAGE:
        ./PlotProbes.py -gene TP53 -out out.png -data Data/methyl_data.txt
