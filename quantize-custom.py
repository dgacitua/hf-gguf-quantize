import sys
import argparse
import subprocess


def print_message(message):
    print("\033[01m{}\033[00m".format(message))


def run_command(command):
    result = subprocess.run(command)

    if result.returncode != 0:
        raise subprocess.CalledProcessError(
            returncode=result.returncode,
            cmd=result.args,
            stderr= result.stderr
        )
    
    return result    


def main():
    try:
        parser = argparse.ArgumentParser(prog="quantize-custom.py",
                                        description="HF model GGUF packer and quantizer")
        
        parser.add_argument("model_id", type=str,
                            help="Hugging Face model id")
        parser.add_argument("-q", "--quant_type", type=str,
                            help="Custom quant type (e.g.: Q8_0)")
        
        args = parser.parse_args()

        if args.quant_type == None:
            print_message("Quant type not set, using Q8_0")
            quant_type = "Q8_0"
        else:
            quant_type = args.quant_type

        model_id = args.model_id
        model_name = model_id.split("/",1)[1]
        quantized_model = f'gguf/{model_name}.{quant_type}.gguf'

        print_message(f'Packing HF model {model_id} to GGUF fp16!')

        command1 = ["python", "./llama.cpp/convert-hf-to-gguf.py", f"models/{model_name}", "--outfile", f"models/{model_name}.fp16.gguf"]
        run_command(command1)

        print_message(f'Preparing {quantized_model} with {quant_type} quantization!')

        command2 = ["./llama.cpp/llama-quantize", f"models/{model_name}.fp16.gguf", quantized_model, quant_type]
        run_command(command2)
    except:
        print_message("An error has occurred!")
    else:
        print_message("Model packing and quantizing successful!")


if __name__ == "__main__":
    main()