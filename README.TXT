===========================================================================
PYMAP PYTHON PACKAGE TO ANALYZE 450K METHYLATION DATA.
===========================================================================

Example pipeline:
#load submodules

import Annotation
import Core

#Load Annotations

annotation_file = "Data/HumanMethylation450_15017482_v1-2.csv"
annotations = Annotation.Annotator()

#load and parse a single methylation file that might contain info for one or more sample.

methyl_file = "EXAMPLE.txt"
samples = Core.ParseFile(methyl_file)

#load and parse multiple methylation files

methyl_directory = "Data/"
samples = Core.ParseFile(methyl_directory)


#get probes associated with a gene

gene= "TP53"
probe_list = annotations.get_probes_from_gene(gene)
print(probe_list)

#get sample name and beta values from parse data

for sample in samples:
    print(sample.name)
    beta_values = sample.probes  # beta_values are loaded from each sample.
