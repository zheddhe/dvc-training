#!/bin/bash
# necessite la librairie dvc avec gdrive (pip install dvc[gdrive])
dvc remote add \
	${1:-remote_storage} \
	gdrive://${2:-1AwphOgPRspY8betr387kSzcYTP893D7r}