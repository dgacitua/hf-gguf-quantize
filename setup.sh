#!/bin/bash

set -euxo pipefail

git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make && pip install -r requirements.txt