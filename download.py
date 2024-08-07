import sys
import argparse
from huggingface_hub import snapshot_download


def print_message(message):
    print("\033[01m{}\033[00m".format(message))


def main():
    try:
        parser = argparse.ArgumentParser(prog="download.py",
                                     description="Hugging Face model download script")
        
        parser.add_argument("model_id", help="Hugging Face model id", type=str)
        parser.add_argument("-t", "--token", help="Hugging Face user token", type=str)
        
        args = parser.parse_args()
        
        model_id = args.model_id
        model_dir = "./models/" + model_id.split("/",1)[1]
        hf_token = args.token

        if hf_token == None:
            snapshot_download(repo_id = model_id,
                            local_dir = model_dir,
                            revision = "main")
        else:
            snapshot_download(repo_id = model_id,
                            local_dir = model_dir,
                            revision = "main",
                            token = hf_token)
    except Exception as error:
        print("An error has occurred!", error)
    else:
        print_message("Model download successful!")


if __name__ == "__main__":
    main()
