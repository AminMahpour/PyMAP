import matplotlib.pyplot as pp


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


class TopList:
    def __init__(self, samples1, samples2):
        """

        :param samples1:
        :param samples2:
        :return:
        """


        pass
