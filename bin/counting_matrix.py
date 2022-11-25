#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys

usage = "Usage: counting_matrix.py /path/to/clinvar_sorted_db"
if len(sys.argv) != 2:
    exit(usage)

input = sys.argv[1]
name = input.split("parsed_")[1].replace(".csv", "")

db = pd.read_csv(input).dropna()
gene_list = list(dict.fromkeys(db['gene_name']))
res = dict()


def counting_matrix(gene, features):
    df_count = db[(db['gene_name'] == gene)][['gene_name', features]]
    unique, counts = np.unique(df_count[features], return_counts=True)
    res[gene][features] = dict(zip(unique, counts))
    return res


def parse_res(res):
    res_dict = dict()
    for a, b in res.items():
        res_dict[a] = dict()
        for c, d in b.items():
            for e, f in d.items():
                res_dict[a][e] = f
    res_table = pd.DataFrame.from_dict(res_dict).T
    res_table.to_csv(name + '_counted.csv')


for gene in gene_list:
    res[gene] = dict()
    for features in ['variant_type', 'significance']:
        counting_matrix(gene, features)
parse_res(res)
