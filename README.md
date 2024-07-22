# hf-gguf-quantize

Toolkit to download, quantize and package Hugging Face models as GGUF.

## Requirements

- Access to a bash terminal
- Python 3.10 (or higher)
- git
- Compilation tools to build llama.cpp
- An installed acceleration framework (CUDA, Metal, and OpenBLAS are currently supported)

## Instructions

### Install

1. Clone repo or download it as ZIP.
2. Run one of the `setup` bash scripts to install llama.cpp with proper acceleration support (`setup-cuda.sh` for CUDA, `setup-openblas.sh` for OpenBLAS, and `setup.sh` for Metal).
3. Run `./update-convert.sh <hf_token>` to update llama.cpp's convert definitions. Replace `<hf_token>` with a Hugging Face token from your account.

### Download model

1. Run `python download.py <model_id> -t <hf_token>` to download a model from Hugging Face. Replace `<model_id>` with a proper HF model id (e.g.: `tiiuae/falcon-7b`) and `<hf_token>` with a Hugging Face token from your account. Models are downloaded under the `models/` folder.

### Quantize and package model

1. Once the model is downloaded, run one of the `quantize` Python scripts to quantize the model and package it as GGUF (replace `<model_id>` with a proper HF model id):
```bash
python quantize-8bit.py <model_id>  # For Q8_0 quants
python quantize-5bit.py <model_id>  # For Q5_K_M quants
python quantize-4bit.py <model_id>  # For Q4_K_M quants
python quantize-custom.py <model_id> -q <quant_type>  # For custom quants specified under <quant_type>
```

2. If the packaging ends succesfully, the GGUF models will be available on the `gguf/` folder.
3. You can delete any `<model_id>.fp16.gguf` models on the `models/` folder, they are no longer needed.


## References

- https://mlabonne.github.io/blog/posts/Quantize_Llama_2_models_using_ggml.html
- https://colab.research.google.com/drive/13dVitv_DBCTprbCarKwFJdf8qG76y6hD?usp=sharing
- https://github.com/ggerganov/llama.cpp/pull/1684


## License

MIT