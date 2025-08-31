#!/bin/bash
# -d : deps (entrées)
# -o : outs (sorties)
dvc stage add -n train \
	-d src/models/train_model.py \
	-d data/preprocessed \
	-o models/trained_model.joblib \
	python src/models/train_model.py