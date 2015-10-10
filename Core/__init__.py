import os

class ParseConfig:
    def __init__(self):
        self.cutoff = None


class Sample:
    def __init__(self):
        self.name = None
        self.probes = None


class Parse:
    def __init__(self, file, delim="\t"):
        self.file = os.path.abspath(file)
        self.delim = delim
        self.beta_list = {}
        self.filternan = True
        self.sample_number = None
        self.samples = []

        # Run analysis
        self.run()

    def run(self):
        """
        Let the parsing process begin.
        :return: Returns nothing.
        """
        sample_list = []
        for i in open(self.file, mode="r"):
            if i.startswith("TargetID"):
                samples = i.replace(".AVG_Beta", "").strip("\n").strip("\r").strip(self.delim).split(self.delim)
                sample_list = samples[1:]
                self.sample_number = len(samples[1:])

            if i.startswith("cg"):
                currentbeta = i.strip("\n").strip("\r").strip(self.delim).split(self.delim)
                bet = currentbeta[1:]
                if len(bet) != self.sample_number:
                    continue
                betas = []
                for k in bet:
                    if k == "" or k == " ":
                        # ignore probes that their beta values are missing even in one sample.
                        # print(i)
                        continue

                    formatted = float(k)
                    betas.append(formatted)

                # Remove beta values that do not cover all samples. Temporary remedy?
                if len(betas) == len(sample_list):
                    betadic = {currentbeta[0]: betas}
                    self.beta_list.update(betadic)
                    ###

        for i, j in enumerate(sample_list):
            sam = Sample()
            sam.name = j
            sam.probes = {k: self.beta_list[k][i] for k in self.beta_list}
            self.samples.append(sam)

    def get_id_beta(self):
        """
        Get all beta values.
        :return:
        """
        return self.beta_list

    def get_all_beta(self):
        """
        Get
        :return:
        """
        listx = []
        for key in self.beta_list.keys():
            out = self.beta_list[key]
            listx.append(out)
        return listx

    def get_probe_avg(self, probe_id, verbose=False):
        """
        Get Probe AVG values.
        :param probe_id: A list of probe ids.
        :return: A list of avg beta values.
        """
        if verbose:
            print("Probe id: %s" % probe_id)
            print("Sample", "\t", "Beta Avg")

        for i, j in enumerate(self.samples):
            sample = j
            beta_val = self.beta_list[probe_id][i]

            if verbose:
                print(sample.name, "\t", beta_val)

        return self.beta_list[probe_id]

    def get_probes_avg(self, probe_id_list):
        """
        Get probe AVG beta values from a list of probes for all samples
        :param probe_id_list: A list of probe ids.
        :return: A list of beta values.
        """
        out = []

        for i in probe_id_list:
            try:
                out.append(self.get_probe_avg(i))
            except Exception as ex:
                pass
        return out

    def samples_to_bed(self, base_filename, probes, samples):
        for sample in samples:
            self.probes_to_bed("%s-%s.bed" % (base_filename, sample.name), probes, sample)

    def probes_to_bed(self, filename, probes, sample):
        """
        Writes a BED file containing the probe beta info.
        :param filename: A filename to be stored.
        :param probes: A list of Probe info
        :param sample_no: The sample number to include in the BED file.
        :return:
        """
        # lets parse some probe here.
        out = open(filename, mode="w")
        out.write('''track name="%s" description="Methylation" visibility=2 itemRgb="On" useScore=1\n''' % sample.name)
        for probe in probes:


            beta_val = None
            try:
                beta_val = float(sample.probes[probe.id])
            except Exception as ex:
                print(ex.args)
                print("%s not found in %s." % (probe.id, sample.name))
                continue

            sign = None
            if probe.strand == "F":
                sign = "+"
            else:
                sign = "-"

            r = int(beta_val * 255)
            g = 0
            b = 0
            out_line = "chr%s\t%d\t%d\t%s\t%f\t%s\t%d\t%d\t%d,%d,%d\n" % (
                probe.chr, probe.cord - 1, probe.cord + 1, probe.id, beta_val, sign, 0, 0, r, g, b)
            out.write(out_line)
        out.close()
        print("%s successfully processed. " % filename)

    def get_sample_by_no(self, sample_no):
        """
        Returns a sample by number [zero based].
        :param sample_no:
        :return:
        """
        return self.samples[sample_no]

    def get_sample_by_name(self, sample_name):
        """
        Returns a sample by name.
        :param sample_name:
        :return:
        """
        selected_sample = None
        for i in self.samples:
            if i.name == sample_name:
                selected_sample = i
                break
        return selected_sample

    def get_all_sample_name(self):
        """
        Get all sample name.
        :return: A list that contain sample names.
        """
        sample_list = []
        for i in self.samples:
            sample_list.append(i)
        return sample_list
