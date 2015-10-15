import Core
import Core.Stats
import Plot
import Annotation

annotation_file = "Data/HumanMethylation450_15017482_v1-2.csv"

annotations = Annotation.Annotator()
print (annotations.get_number())
annotations.remove_snp_probes()
print (annotations.get_number())


#print( annotations.get_probes_id_from_chr_loc (Annotation.chr_loc("12",123234099,123242197)))


#samples = Core.ParseBatch("Data/").get_all_samples()


file = "Data/GSE42308.txt"
samples = Core.ParseFile(file).get_sample()

#print(samples)


#Core.Stats.Dist(parse.get_probes_avg(annotations.get_probes_id_from_loc(Annotation.Location.BODY)), [0, 1, 2, 3, 4, 5], parse.samples)
probe_list = annotations.get_probes_from_gene("BRCA1")

print(len(probe_list))
for i in probe_list:
    print(i.cord)

print("sort data...")
probe_list = annotations.sort_coord_probe(probe_list)
for i in probe_list:
    print(i.cord)
print(len(probe_list))

Core.write_data("data.txt", samples, probe_list)
#prop = Plot.properties()
#prop.size=30
Plot.Heatmap(samples, probe_list, "gello.png")

#probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

#parse.probes_to_bed("Export/test2.bed", probe_list, parse.samples[0])
#parse.samples_to_bed("Export/me", probe_list, parse.samples)


#s1 = [parse.get_sample_by_no(0), parse.get_sample_by_no(1), parse.get_sample_by_no(2)]
#s2 = [parse.get_sample_by_no(3), parse.get_sample_by_no(4), parse.get_sample_by_no(5)]

#print (Core.Stats.TopList(s1,s2,annotations.get_probes_all()).get())