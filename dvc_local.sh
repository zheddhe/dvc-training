#!/bin/bash
dvc remote add \
	${1:-remote_storage} \
	${2:-../dvc_local}