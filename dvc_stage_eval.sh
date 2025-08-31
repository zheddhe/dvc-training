#!/bin/bash
# -d : deps (entrées)
# -M : metrics (sortie métrique)
dvc stage add -n evaluation \
	-d src/models/evaluate_model.py \
	-d models/trained_model.joblib \
	-M metrics/accuracy.json \
	python src/models/evaluate_model.py