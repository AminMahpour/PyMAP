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
parser.add_argument("-gene", help="Name of gene that probe id will be returned for")
parser.add_argument("-out", help="get output with [y]")

args = vars(parser.parse_args())

annotations = Annotation.Annotator()
probes = annotations.get_probes_from_gene(args["gene"])


for i in probes:
    print(i.id)

if args["out"] == "y" or args["out"] == "Y":
    out_file = open("%s-probes.txt" % args["gene"], mode="w")
    for i in probes:
        out_file.write("%s\n"%i.id)
    out_file.close()


if len(probes) == 0 :
    print("Your gene did not return a valid probe id")
