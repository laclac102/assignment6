#!/usr/bin/env python3

import pandas as pd
import re
import sys
usage = "Usage: parse_clinvar.py /path/to/clinvar_database"
if len(sys.argv) != 2:
    exit(usage)
data = sys.argv[1]

df = pd.read_csv(data, skiprows=27, sep='\t')
target = df[(df['#CHROM'] == 13) & (
    df['POS'] <= 36000000) & (df['POS'] >= 26000000)]
info = target.INFO.str.split(";", expand=True)

info_dict = info.T.to_dict()
res = dict()
regex = {
    "gene_name": "GENEINFO=",
    "diseases": "CLNDN=",
    "significance": "CLNSIG=",
    "variant_type": "MC=",
    "rs_ID": "RS="
}
for a, b in info_dict.items():
    res[a] = dict()
    for c, d in b.items():
        for key, val in regex.items():
            key_val = re.search(val, str(d))
            if key_val:
                res[a][key] = key_val.string.replace(val, "")

clinvar = pd.DataFrame.from_dict(res, orient="index")
clinvar = clinvar.assign(
    CHROM=df['#CHROM'], POS=df['POS'], REF=df['REF'], ALT=df['ALT'])
# clinvar.info()
for i in range(len(clinvar['variant_type'])):
    match = re.search("SO:........", str(clinvar['variant_type'].iloc[i]))
    if match:
        clinvar['variant_type'].iloc[i] = clinvar['variant_type'].iloc[i].replace(
            match.group(0), "")

clinvar['gene_name'] = clinvar['gene_name'].str.split(":").str[0]
clinvar = clinvar[['CHROM', 'POS', 'REF', 'ALT', 'diseases',
                   'significance', 'gene_name', 'variant_type', 'rs_ID']]
clinvar.sort_values(by=['POS'])
clinvar.to_csv("parsed_assignment6_db.csv")
