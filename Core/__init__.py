import os


class ParseConfig:
    def __init__(self):
        self.cutoff = None


class Sample:
    """

    Sample data object.
    Each *sample* has a name which is a string type and Probe methylation data which is a dictionary type.

    :param name: Name of the sample.
    :param probes: methylation data of the sample - in dict type.

    """
    def __init__(self, name=None, probes=None):
        self.name = name
        self.probes = probes


class ParseBatch:
    """

    Parse a series of data in a folder.

    :param folder: A string that represent a folder.
    :param delim: delimitation character used in the data file [default = tab].
    :param avg_beta_header: A string that represents average beta values [default = .AVG_Beta].
    :return: A ParseBatch object. Use get_samples() function to retrieve sample information.


    """

    def __init__(self, folder, delim="\t", avg_beta_header=".AVG_Beta"):
        self.folder = folder
        self.samples = []
        self.delim = delim
        self.avg_header = avg_beta_header
        for file in os.listdir(os.path.abspath(self.folder)):
            if file.endswith(".txt"):

                # Parse file.

                parsed_file = ParseFile(os.path.abspath(os.path.join(self.folder, file)), delim=self.delim,
                                        avg_beta_header=self.avg_header).get_samples()

                self.samples.extend(parsed_file)

        print("%d samples processed." % len(self.samples))
        for i in self.samples:
            print(i.name)

    def get_samples(self):
        """

        Return all sample objects created from all files

        """
        return self.samples


class ParseFile:
    """

    Parse a single file. The file could still have multiple samples. This module automatically finds and parses them.

    :param filename: A string that represent a data file name.
    :param delim: delimitation character used in the data file [default = tab].
    :param avg_beta_header: A string that represents average beta values [default = .AVG_Beta].
    :return: A ParseFile object. Use get_samples() function to retrieve sample information.

    """

    def __init__(self, filename, delim="\t", avg_beta_header=".AVG_Beta"):

        self.delim = delim
        name_cols = []
        avg_cols = []
        beta_vals = []
        self.samples = []

        # Check weather the file exists.

        if self.check_file(filename):

            # Open the file and parse the content.

            for line in open(filename, mode="r"):

                # Parse a single file content.

                if line.startswith("TargetID"):
                    cols = line.strip("\n").strip("\r").split(self.delim)
                    for i, col in enumerate(cols):
                        if col.endswith(avg_beta_header):
                            name_cols.append(col.strip(avg_beta_header))
                            avg_cols.append(i)
                    beta_vals = []
                    for i in avg_cols:
                        beta_vals.append({})
                if line.startswith("cg"):
                    cols = line.strip("\n").strip("\r").split(self.delim)
                    for i, avg_col in enumerate(avg_cols):
                        average = cols[avg_col].strip()
                        if average is not None and average != "":
                            average = float(average)
                            beta_vals[i].update({cols[0]: average})

            # Create Samples.

            for i, betas in enumerate(beta_vals):
                samples_file = Sample(name=name_cols[i], probes= betas)
                self.samples.append(samples_file)

        else:
            print("Critical Error: File not found.")

    def get_samples(self):
        """

        Returns all samples in this file.

        """
        return self.samples

    def check_file(self, filename):
        """

        Check input filename

        :param filename: A string that represents a data file.
        :return: A boolean value.

        """
        return os.path.isfile(os.path.abspath(filename))


def get_id_beta(sample):
    """

    Get all beta values.

    :return: return beta values of a sample.

    """
    return sample.probes


def get_all_beta(sample):
    """

    Get all beta values.

    :return: A list of beta

    """
    listx = []
    for key in sample.probes.keys():
        out = sample.probes[key]
        listx.append(out)
    return listx


def get_probe_avg(probe_id, samples, verbose=False):
    """

    Get Probe AVG values.

    :param probe_id: A list of probe ids.
    :return: A list of avg beta values.

    """
    beta_val = []
    if verbose:
        print("Probe id: %s" % probe_id)
        print("Sample", "\t", "Beta Avg")

    for i, sample in enumerate(samples):
        beta_val.append(sample.probes[probe_id])

        if verbose:
            print(sample.name, "\t", beta_val)

    return beta_val


def get_probes_avg(probe_id_list, sample):
    """

    Get probe AVG beta values from a list of probes for all samples

    :param probe_id_list: A list of probe ids.
    :return: A list of beta values.

    """
    out = []

    for i in probe_id_list:
        try:
            out.append(sample.probes(i))
        except Exception as ex:
            pass
    return out


def samples_to_bed(base_filename, probes, samples):
    """

    Return a BED file representative of all samples for the provided probes.

    :param base_filename: A base name for output file
    :param probes: A list of probes objects.
    :param samples: A list of samples to extract data.
    :return: Static function - stores a file.

    """
    for sample in samples:
        probes_to_bed("%s-%s.bed" % (base_filename, sample.name), probes, sample)


def probes_to_bed(filename, probes, sample):
    """

    Writes a BED file containing the probe beta info.

    :param filename: A filename to be stored.
    :param probes: A list of Probe info.
    :param sample_no: The sample number to include in the BED file.
    :return: Static function - stores a file.

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


def get_sample_by_no(samples, sample_no):
    """

    Returns a sample by number [zero based].

    :param sample_no: Sample number, a zero based integer.
    :return: Return a sample object.

    """
    return samples[sample_no]


def get_sample_by_name(samples, sample_name):
    """

    Returns a sample by name.

    :param sample_name: Sample name, a string.
    :return: Return a sample object.

    """
    selected_sample = None
    for i in samples:
        if i.name == sample_name:
            selected_sample = i
            break
    return selected_sample


def get_all_sample_name(samples):
    """

    Get all sample name.

    :return: A list that contain sample names.

    """
    sample_list = []
    for i in samples:
        sample_list.append(i)
    return sample_list


def get_genes_from_probes(probe_list):
    """

    Get gene names and number of probes associated with each gene.

    :param probe_list: A list of probes.
    :return: A dictionary of genes names and probes numbers.

    """

    gene_dict = {}
    for probe in probe_list:

        if probe.gene in gene_dict:
            gene_dict[probe.gene] += 1
        else:
            gene_dict.update({probe.gene: 1})

    return gene_dict


def write_data(file_name, samples, probes):
    """

    Export data to data table

    :param samples: A list of samples.
    :param probes: A list of probes.
    :return: Writes a data file.

    """
    output_file = open(file_name, mode="w")
    output_file.write("Probe id\t")

    # Header information
    for sample in samples:
        output_file.write("%s\t" % sample.name)
    output_file.write("\n")

    # probe methlation info
    for probe in probes:
        output_file.write("%s\t" % probe.id)

        for sample in samples:
            output_file.write("%s\t" % sample.probes[probe.id])

        output_file.write("\n")
    output_file.close()
