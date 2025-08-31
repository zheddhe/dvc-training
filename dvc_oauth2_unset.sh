#!/bin/bash
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_client_id --unset
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_client_secret --unset