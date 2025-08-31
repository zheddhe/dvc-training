#!/bin/bash
# en local seulement (pas de commit git)
dvc remote modify \
	${1:-origin} \
	--local access_key_id --unset
dvc remote modify \
	${1:-origin} \
	--local secret_access_key --unset