#!/bin/bash
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_use_service_account false
dvc remote modify \
	${1:-remote_gdrive} \
	gdrive_service_account_json_file_path --unset