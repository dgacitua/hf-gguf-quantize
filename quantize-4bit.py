import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quantize-4bit.py <model_id>")
        sys.exit(1)

    model_id = sys.argv[1]
    model_name = model_id.split("/",1)[1]
    quant_type = "Q4_K_M"
    quantized_model = f'gguf/{model_name}.{quant_type}.gguf'

    command1 = ["python", "./llama.cpp/convert-hf-to-gguf.py", f"models/{model_name}", "--outfile", f"models/{model_name}.fp16.gguf"]
    subprocess.run(command1)

    print(f'Preparing {quantized_model} with {quant_type} quantization.')

    command2 = ["./llama.cpp/llama-quantize", f"models/{model_name}.fp16.gguf", quantized_model, quant_type]
    subprocess.run(command2)
