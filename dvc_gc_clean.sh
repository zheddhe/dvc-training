#!/bin/bash
# -w / --workspace : 	Keep data files used in the current workspace
# -c / --cloud : 		Collect garbage in remote storage in addition to local cache
# --dry : 				Only print what would get removed without actually removing
# -r / --remote : 		Remote storage to collect garbage in
dvc gc --workspace --cloud \
	-r ${1:-remote_storage}

# find and delete unused MD5 dirs
find .dvc/cache -type d -empty -delete