# Research Data For Replication

This folder contains a small public dataset for a reproducible-analysis exercise.

The data files come from the `palmerpenguins` project. They are useful because the folder includes both a cleaned teaching dataset and a rawer version of the same measurements. Participants can ask Codex to inspect the variables, compare the two files, document provenance, and create a simple repeatable analysis.

## Files

- `data/penguins.csv` is the simplified teaching dataset.
- `data/penguins_raw.csv` contains the original variable names and a wider set of fields.

## Suggested Exercise

Ask Codex to:

1. Inspect the two CSV files.
2. Create a short data inventory.
3. Identify the key variables and missing values.
4. Propose one simple analysis that can be reproduced from the raw files.
5. Save any code, outputs, and assumptions in separate files.

## Source And Citation

The data are from the public `palmerpenguins` package:

- Project: <https://github.com/allisonhorst/palmerpenguins>
- Dataset documentation: <https://allisonhorst.github.io/palmerpenguins/>
- Package citation: Horst AM, Hill AP, Gorman KB (2020). `palmerpenguins: Palmer Archipelago (Antarctica) penguin data`. R package version 0.1.0. <https://doi.org/10.5281/zenodo.3960218>
- Original paper: Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins. PLoS ONE 9(3): e90081. <https://doi.org/10.1371/journal.pone.0090081>

The `palmerpenguins` repository states that the data are available under a CC0 licence in accordance with the Palmer Station LTER and US LTER data policies.
