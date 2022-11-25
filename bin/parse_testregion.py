#!/usr/bin/env python3

import pandas as pd
import sys

usage = "Usage: parse_testregion.py /path/to/clinvar_sorted_db"
if len(sys.argv) != 3:
    exit(usage)

region = sys.argv[1]

testregion = pd.read_csv(region, sep='\t', names=['CHROM', 'START', 'END'])
clinvar = pd.read_csv(sys.argv[2])

testregion_bases = []
CHR = []
for i in range(len(testregion)):
    pos = testregion.iloc[i]['START']
    while pos < testregion.iloc[i]['END']:
        CHR.append('chr13')
        testregion_bases.append(pos)
        pos += 1

testregion_bases_data = {'#CHROM': CHR, 'POS': testregion_bases}
testregion_df = pd.DataFrame(data=testregion_bases_data)
testregion_merged = testregion_df.merge(
    clinvar, left_on='POS', right_on='POS', how='inner')
testregion_merged.to_csv('parsed_testregion.csv')
