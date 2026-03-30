import os


def export_defense_finder_genes(defense_finder_genes, outdir, filename):
    safe_filename = os.path.basename(filename) + '_defense_finder_genes.tsv'
    defense_finder_genes.to_csv(os.path.join(outdir, safe_filename), sep='	', index=False)