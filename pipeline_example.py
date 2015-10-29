import Core
import Core.Stats
import Plot
import Annotation
import matplotlib.pyplot as pp

annotations = Annotation.Annotator()
print ("probe No:", annotations.get_number())
annotations.remove_snp_probes()
print ("probe No after SNP removal:", annotations.get_number())

file = "Data/GSE42308.txt"
samples = Core.ParseFile(file).get_samples()

# samples2 = Core.ParseBatch("Data/").get_all_samples()


probes = annotations.get_probes(annotations.get_all_probe_ids())
print(len(probes))
probe2 = Annotation.get_probes_from_feature(probes, Annotation.Feature(Annotation.CpG_location.ISLAND))
print(len(probe2))
probe3 = Annotation.get_probes_from_feature(probe2, Annotation.Feature("BRCA1"))
print(len(probe3))

brcaprobes = annotations.get_probes(annotations.get_probes_id_from_gene("BRCA1"))
#groups= [groups[0], groups[3]]
Plot.BoxPlot(probes, samples)

# probe_list = annotations.get_probes_from_gene("TP53")

# probe_list2 =annotations.get_probes_id_from_loc(Annotation.Location.BODY)

# probe_list3 =annotations.get_probes_id_from_cpg(Annotation.CpG_location.NSHORE)

# print(probe_list3)

# sort data
# probe_list = annotations.sort_coord_probe(probe_list)

# Core.write_data("data.txt", groups, probe_list)

Plot.Heatmap(samples, brcaprobes, "brca1.png")
Plot.Heatmap(samples, probe3, "brca2.png")

# pp.plot(groups[0].probes, groups[1].probes)

# pp.show()

# probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

# Core.probes_to_bed("Export/test2.bed", probe_list, groups.groups[0])
# Core.samples_to_bed("Export/me", probe_list, groups)


# s1 = [parse.get_sample_by_no(0), parse.get_sample_by_no(1), parse.get_sample_by_no(2)]
# s2 = [parse.get_sample_by_no(3), parse.get_sample_by_no(4), parse.get_sample_by_no(5)]

# print (Core.Stats.TopList(s1,s2,annotations.get_all_probe_ids()).get())
