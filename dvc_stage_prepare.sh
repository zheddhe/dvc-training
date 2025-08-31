#!/bin/bash
# -d : deps (entrées)
# -o : outs (sorties)
dvc stage add -n prepare \
	-d src/data/make_dataset.py \
	-d data/raw \
	-o data/preprocessed \
	python src/data/make_dataset.py