#!/bin/bash
# en local seulement (pas de commit git)
dvc remote modify \
	${1:-remote_gdrive} \
	--local gdrive_client_id --unset
dvc remote modify \
	${1:-remote_gdrive} \
	--locam gdrive_client_secret --unset