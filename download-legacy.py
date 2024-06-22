import os
import sys
import torch
import requests
from transformers import AutoModelForCausalLM


def download_file_from_huggingface(model_id, filename, save_path):
    url = f"https://huggingface.co/{model_id}/resolve/main/{filename}"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to download {filename}.HTTP Status Code: {r.status_code}")
        return False
    with open(os.path.join(save_path, filename), "wb") as f:
        f.write(r.content)
    return True


def run(model_id):
    files_to_download = [
        "tokenizer_config.json",
        "tokenizer.model",
        "tokenizer.json",
        "special_tokens_map.json",
        "added_tokens.json",
    ]

    # Create the directory if it doesn't exist
    save_path = "./models/" + model_id.split("/",1)[1]

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Download the files
    for filename in files_to_download:
        success = download_file_from_huggingface(model_id, filename, save_path)
        if success:
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download-legacy.py <model_id>")
        sys.exit(1)

    model_id = sys.argv[1]
    model_dir = "./models/" + model_id.split("/",1)[1]

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
    )

    model.save_pretrained(
        model_dir,
        safe_serialization=False,
    )

    run(model_id)
