#! /usr/bin/env bash

set -e

uvicorn "sources.main:application" --host "0.0.0.0" --port 8000 --reload
