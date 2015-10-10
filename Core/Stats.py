import matplotlib.pyplot as pp
import scipy.stats as statsx
from threading import Thread
import threading

class Transform:
    def __new__(cls, beta_list, sample_id, lab):
        fl = []
        for j in sample_id:
            l = [i[j] for i in beta_list if len(i) == len(sample_id)]
            fl.append(l)
        return fl

class Dist:
    def __init__(self, beta_list, sample_id, lab):
        fl = Transform(beta_list, sample_id, lab)
        pp.boxplot(fl, labels=[i.name for i in lab])
        pp.show()

class Plot:
    def __init__(self, samples, beta_list):
        no = list(range(0, len(samples)))
        print(no)
        print(len(beta_list))
        pp.boxplot(beta_list, labels=samples)
        # pp.xticks(samples)
        pp.show()

class Ttest(threading.Thread):
    def __init__(self,sample1, sample2, probe, diff_id_list):
            threading.Thread.__init__(self)
            self.sample1 = sample1
            self.sample2 = sample2
            self.probe = probe
            self.diff_id_list = diff_id_list

    def run(self):
        sample1_betas = []
        sample2_betas = []

        for sam1 in self.sample1:
            sample1_betas.append(sam1.probes[self.probe])
        for sam2 in self.sample2:
            sample2_betas.append(sam2.probes[self.probe])
        #print(sample1_betas)
        #print(sample2_betas)

        (t, pval) = statsx.ttest_ind(sample1_betas, sample2_betas)
        #print(float(pval))

        if float(pval) < float(0.05):
            self.diff_id_list.append(self.probe)
            print ("DOONEEE")



class TopList:
    def __init__(self, samples1, samples2, all_probes):
        """
        Returns differentially methylated probes among sample 1 and 2
        :param samples1: list of sample 1
        :param samples2: list of sample 2
        :return: a list of probes ids
        """
        self.samples1 = samples1
        self.samples2 = samples2


        self.diff_probe_id = []
        no_probe_processed = 0
        for probe in all_probes:
            try:
                #t = Thread(target= self.ttest, args = (self.samples1, self.samples2, probe))
                #t.start()
                back = Ttest(self.samples1, samples2, probe, self.diff_probe_id)
                back.run()

            except Exception as ex:
                continue
            finally:
                no_probe_processed += 1
                print(no_probe_processed)




            #input()

    def ttest(self,samples1, samples2, probe):
        sample1_betas = []
        sample2_betas = []

        for sam1 in samples1:
            sample1_betas.append(sam1.probes[probe])
        for sam2 in samples2:
            sample2_betas.append(sam2.probes[probe])
        #print(sample1_betas)
        #print(sample2_betas)

        (t, pval) = statsx.ttest_ind(sample1_betas, sample2_betas)
        #print(float(pval))

        if float(pval) < float(0.05):
            self.diff_probe_id.append(probe)


    def get(self):
        return self.diff_probe_id

