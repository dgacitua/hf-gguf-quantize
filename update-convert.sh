#!/bin/bash

set -euxo pipefail

cd llama.cpp && git reset --hard HEAD && git pull && python convert_hf_to_gguf_update.py $1