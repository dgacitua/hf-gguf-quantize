#!/bin/bash

set -euxo pipefail

cd llama.cpp && python convert-hf-to-gguf-update.py $1