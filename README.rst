
PYMAP PYTHON PACKAGE TO ANALYZE 450K METHYLATION DATA.
======================================================
PyMAP is a python package for efficient and fast analyzing of Illumina 450K methylation data.

Examples and Documentations
===========================
Please head over to http://pymap.readthedocs.org for examples and detailed documentations of the pyMAP package.


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
