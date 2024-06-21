#!/bin/bash

set -euxo pipefail

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && LLAMA_CUDA=1 make && pip install -r requirements.txt