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

#load single methylation file

methyl_file = "EXAMPLE.txt"
Core.ParseFile(methyl_file)

#load multiple methylation files

methyl_directory = "Data/"
Core.ParseFile(methyl_directory)


#get probes associated with a gene

gene= "TP53"
probe_list = annotations.get_probes_from_gene(gene)
print(probe_list)

