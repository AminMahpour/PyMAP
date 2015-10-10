#!/usr/bin/env python

import argparse
import Core
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
parser.add_argument("-file", help="File name that contains average beta values.")
parser.add_argument("-out", help="directory that BED files will be stored.")
parser.add_argument("-gene", help="Name of gene that BED file will be created for")
args = vars(parser.parse_args())


file = os.path.abspath(args["file"])
out = os.path.abspath (args["out"])

if check_file( file) :
    annotations = Annotation.Annotator()
    parse = Core.ParseFile(file)
    probe_list = annotations.get_probes_from_gene( args["gene"])

    Core.samples_to_bed(out, probe_list, parse.samples)
    print("Done.")

else:
    print("File does not exist.")
