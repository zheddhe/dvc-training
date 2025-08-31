#!/bin/bash
# en local seulement (pas de commit git)
dvc remote modify origin \
	--local access_key_id ${1:-access_key_id} 
dvc remote modify origin \
	--local secret_access_key ${2:-secret_access_key}