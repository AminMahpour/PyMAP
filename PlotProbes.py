#!/usr/bin/env python

import argparse
import Core
import Plot
import Annotation
import os


def check_file(filename):
    """
    Chech for the existance of the input filename.
    :param filename: filename to check.
    :return:
    """
    return os.path.exists( os.path.abspath(filename))

# USAGE : ./convertbed.py -file Data/GSE42308.txt -out gello.bed -gene DENR
parser = argparse.ArgumentParser()
parser.add_argument("-gene", help="Name of gene that probe id will be returned for")
parser.add_argument("-data", help="Name of file that methylation data is stored.")
parser.add_argument("-out", help="Output image name")

args = vars(parser.parse_args())

annotations = Annotation.Annotator()
probes = annotations.get_probes_from_gene(args["gene"])
samples = Core.ParseFile(args["data"]).get_sample()

Plot.Heatmap(samples, probes , args["out"])

if len(probes) == 0:
    print("Your gene did not return a valid probe id")
