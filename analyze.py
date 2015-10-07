import Core
import Core.Parse
import Core.Stats
import Annotation

annotation_file = Core.File("Data/HumanMethylation450_15017482_v1-2.csv")
annotations = Annotation.Annotator(annotation_file)

file = Core.File("Data/GSE42308.txt")
parse = Core.Parse.Parse(file)

#Core.Stats.Dist(parse.get_probes_avg(annotations.get_probes_id_from_loc(Annotation.Location.BODY)), [0, 1, 2, 3, 4, 5], parse.samples)
probe_list = annotations.get_probes_from_gene("DENR")
#probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

parse.probes_to_bed("Export/test.bed", probe_list, parse.samples[0])
