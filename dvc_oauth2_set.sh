#!/bin/bash
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_client_id "${2:-gdrive_client_id}"
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_client_secret "${3:-gdrive_client_secret}"