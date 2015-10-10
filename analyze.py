import Core
import Core.Stats
import Annotation

#annotation_file = "Data/HumanMethylation450_15017482_v1-2.csv"
#annotations = Annotation.Annotator()

Core.ParseBatch("Data/")


#file = "Data/GSE42308.txt"
#parse = Core.Parse(file)

#Core.Stats.Dist(parse.get_probes_avg(annotations.get_probes_id_from_loc(Annotation.Location.BODY)), [0, 1, 2, 3, 4, 5], parse.samples)
#probe_list = annotations.get_probes_from_gene("DENR")
#probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

#parse.probes_to_bed("Export/test2.bed", probe_list, parse.samples[0])
#parse.samples_to_bed("Export/me", probe_list, parse.samples)


#s1 = [parse.get_sample_by_no(0), parse.get_sample_by_no(1), parse.get_sample_by_no(2)]
#s2 = [parse.get_sample_by_no(3), parse.get_sample_by_no(4), parse.get_sample_by_no(5)]

#print (Core.Stats.TopList(s1,s2,annotations.get_probes_all()).get())