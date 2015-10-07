import Core
import Core.Parse
import Core.Stats
import Annotation

annotation_file = Core.File("Data/HumanMethylation450_15017482_v1-2.csv")
annotations = Annotation.Annotator(annotation_file)
annotations.run()

file = "Data/GSE42308.txt"
file = Core.File(file)
parse = Core.Parse.Parse(file)
parse.get_all_beta()

#Core.Stats.Dist(parse.get_probes_avg(annotations.get_probes_loc( Annotation.Location.TSS200)), [0, 1, 2, 3, 4, 5], parse.sample_list)
probe_list = annotations.get_probes(annotations.get_probes_id_from_gene("DENR"))
#probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

#print(parse.sample_list[1].probes)
parse.probes_to_bed("Export/test.bed", probe_list, parse.samples[0])
