class Probe:
    """
    This class holds probe info.
    """

    def __init__(self):
        self.id = None
        self.seq = None
        self.name = None
        self.chr = None
        self.cord = None
        self.strand = None
        self.gene = None
        self.refseq = None
        self.beta = None
        self.tour = None


class Location:
    """
    Probe location is defined here.
    """
    BODY = "Body"
    TSS200 = "TSS200"
    TSS1500 = "TSS1500"
    UTR5 = "5'UTR"
    UTR3 = "3'UTR"
    EXON = "Exon"


class CpG_location:
    """
    CpG location is defined here.
    """
    ISLAND = "Island"
    NSHORE = "N_Shore"
    SSHORE = "S_Shore"
    NSHELF = "N_Shelf"
    SSHELF = "S_Shelf"


class Annotator:
    """
    This class parse all information about Illumina probes.
    """

    def __init__(self, ann):
        self.ann = ann
        self.probe = {}

    def run(self):
        """
        Run the annotation initial setup.
        :return:
        """
        for i in open(self.ann, mode="r"):
            if i.startswith("cg"):
                data = i.split(",")
                # Assigning probe information.
                new_probe = Probe()
                new_probe.id = data[0]
                new_probe.name = data[1]
                new_probe.seq = data[13]
                new_probe.chr = data[11]
                new_probe.cord = int(data[12])
                new_probe.strand = data[16]
                new_probe.gene = data[21].split(";")
                new_probe.refseq = data[22]
                new_probe.loc = data[23].split(";")
                new_probe.tour = data[25]
                newcpg = {new_probe.id: new_probe}
                self.probe.update(newcpg)
        return self.probe

    def get_probes_gene(self, gene_name):
        probes = {k: self.probe[k] for k in self.probe if gene_name in self.probe[k].gene}
        return self.get_keys(probes.keys())

    def get_probes_loc(self, probe_loc):
        probes = {k: self.probe[k] for k in self.probe if probe_loc in self.probe[k].loc}
        return self.get_keys(probes.keys())

    def get_probes_cpg(self, cpg_loc):
        probes = {k: self.probe[k] for k in self.probe if cpg_loc in self.probe[k].tour}
        return self.get_keys(probes.keys())

    def get_id_probe(self, probe_list):
        return self.get_keys(probe_list.keys())

    def get_keys(self, dic_keys):
        """
        Get Probe id from probe dictionaries
        :param dic_keys: Probe dict.
        :return: returns a list of probe id.
        """
        l = []
        for i in dic_keys:
            l.append(i)

        return l

    def get_probe(self, probe_id):
        """
        This function returns the info associated with an id.
        :param probe_id: ILLUMINA ID
        :return: all info
        """

        try:
            probe = self.probe[probe_id]
        except Exception as ex:
            probe = None
            print("WARNING: No probe with id of %s found." % probe_id)
        return probe

    def get_probes(self, list_of_ids):
        """
        This function returns a list of probe info from a list of ids.
        :param list_of_ids:
        :return:
        """
        out_list = []
        for probe_id in list_of_ids:
            out_list.append(self.get_probe(probe_id))

        return out_list
