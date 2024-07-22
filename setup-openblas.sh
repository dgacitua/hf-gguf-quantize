#!/bin/bash

set -euxo pipefail

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && LLAMA_OPENBLAS=1 make && pip install -r requirements.txt

pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes