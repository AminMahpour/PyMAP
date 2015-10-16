import Core
import Core.Stats
import Plot
import Annotation
import matplotlib.pyplot as pp
annotations = Annotation.Annotator()
print (annotations.get_number())
annotations.remove_snp_probes()
print (annotations.get_number())



file = "Data/GSE42308.txt"
samples = Core.ParseFile(file).get_sample()
probe_list = annotations.get_probes_from_gene("TP53")

print(probe_list)

#sort data
probe_list = annotations.sort_coord_probe(probe_list)


Core.write_data("data.txt", samples, probe_list)
Plot.Heatmap(samples, probe_list, "gello.png")

pp.plot(samples[0].probes, samples[1].probes)

pp.show()

#probe_list = annotations.get_probes(["cg06976222", "cg00311963", "cg01061520"])

#parse.probes_to_bed("Export/test2.bed", probe_list, parse.samples[0])
#parse.samples_to_bed("Export/me", probe_list, parse.samples)


#s1 = [parse.get_sample_by_no(0), parse.get_sample_by_no(1), parse.get_sample_by_no(2)]
#s2 = [parse.get_sample_by_no(3), parse.get_sample_by_no(4), parse.get_sample_by_no(5)]

#print (Core.Stats.TopList(s1,s2,annotations.get_probes_all()).get())

