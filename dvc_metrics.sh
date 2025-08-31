#!/bin/bash
# on peut donner un nom d'étape pour reproduire uniquement la pipeline sur celle ci
dvc repro \
	${@:1}