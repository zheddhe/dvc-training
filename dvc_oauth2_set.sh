#!/bin/bash
# en local seulement (pas de commit git)
dvc remote modify \
	${1:-remote_gdrive} \
	--local gdrive_client_id ${2:-gdrive_client_id}
dvc remote modify \
	${1:-remote_gdrive} \
	--local gdrive_client_secret ${3:-gdrive_client_secret}