import os
import pandas as pd
from bed_reader import open_bed, sample_file


def get_data(gene_exp_fp, pop_file, plink_bed, plink_bim, plink_fam, desired_pop):
    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
    '''
    gene_exp_data = pd.read_csv(gene_exp_fp)
    gene_expression_22 = gene_expression[gene_expression['Chr'] == '22']
    gene_t = gene_expression_22.melt(list(gene_expression_22.columns[:4]), var_name='sample_id', value_name='Value')
    pop = pd.read_csv(pop_file, sep = ' ')
    pop = pop.rename(columns ={'sample': 'sample_id'})
    exp_pop = gene_t.merge(pop, on = "sample_id", how = "outer").dropna()
    exp_pop  = exp_pop[['Gene_Symbol', 'Coord', 'sample_id', 'Value', 'group']]
    bed = open_bed(plink_bed)
    val2 = bed.read()
    bim_file = pd.read_csv(plink_bim, sep='\t', header=None, 
            names=['CHR', 'SNP', 'GP', 'POS', 'A1', 'A2'])
    gene_list = gene_expression_22['Gene_Symbol']
    sample_ids = bed.iid
    return gene_list, sample_ids, exp_pop, val2, bim_file, desired_pop
