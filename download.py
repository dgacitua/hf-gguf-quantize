import sys
from huggingface_hub import snapshot_download

if len(sys.argv) != 2:
    print("Usage: python download.py <model_id>")
    sys.exit(1)

model_id = sys.argv[1]
model_dir = "./models/" + model_id.split("/",1)[1]

snapshot_download(repo_id = model_id,
                  local_dir = model_dir,
                  revision = "main")