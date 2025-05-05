import pandas as pd
import numpy as np
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns
import tempfile
import os
import qiime2
from qiime2.plugin import Visualization
from qiime2.plugin.util import transform

def sequence_length_visualizer(table: qiime2.Artifact, sequences: qiime2.Artifact) -> Visualization:
    # Convert feature table to DataFrame
    table_df = table.view(pd.DataFrame)

    # Convert sequences to a dictionary {id: sequence}
    seq_dict = sequences.view(dict)

    # Calculate sequence lengths
    lengths = [len(str(seq)) for seq in seq_dict.values()]

    # Calculate stats
    min_len = int(np.min(lengths))
    max_len = int(np.max(lengths))
    mean_len = round(np.mean(lengths), 2)
    std_len = round(np.std(lengths), 2)

    # Output stats file
    tmp_dir = tempfile.mkdtemp()
    stats_path = os.path.join(tmp_dir, "length_stats.txt")
    with open(stats_path, "w") as f:
        f.write(f"Min Length: {min_len}\n")
        f.write(f"Max Length: {max_len}\n")
        f.write(f"Mean Length: {mean_len}\n")
        f.write(f"Standard Deviation: {std_len}\n")

        # Optional: Quality control warning
        expected_min, expected_max = 250, 300
        outlier_count = sum(l < expected_min or l > expected_max for l in lengths)
        if outlier_count / len(lengths) > 0.95:
            f.write("\nWARNING: Over 95% of reads fall outside expected V4 region (250–300bp)\n")

    # Plot histogram
    hist_path = os.path.join(tmp_dir, "length_histogram.png")
    sns.histplot(lengths, bins=50)
    plt.title('Sequence Length Distribution')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.savefig(hist_path)
    plt.close()

    # Return as QIIME2 visualization
    return Visualization._from_data_dir(tmp_dir)
