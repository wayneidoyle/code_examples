# Plots histogram of base qualities
# When invoked by a Snakemake fule an object called snakemake is passed in
#   All properties from the rule are kept as attributes (input, output, wildcards, etc.)
#   snakemake.input and snakemake.output are always lists, no matter how many values are present

# Load modules
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

# Get base qualities from rule inputs
quals = [record.qual for record in VariantFile(snakemake.input[0])]

# Plot histogram
plt.hist(quals)

# Save figure
plt.savefig(snakemake.output[0])