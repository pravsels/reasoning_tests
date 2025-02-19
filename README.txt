

create conda environment
```
conda create -n r1_tests python==3.10
```

install requirements 
```
pip install -r requirements.txt 
```

dload the model 
```
python dload.py 
```

convert model to gguf format
```
python convert_hf_to_gguf.py --outfile deepseek_r1_llama_8b.gguf DeepSeek_R1_LLAMA_8B
```

build llama.cpp 
```
# Create and enter build directory
mkdir build
cd build

# Generate build files
cmake ..

# Build the project
cmake --build . --config Release
```

Run the model 
```
cd build/bin/

./llama-cli -m ../../deepseek_r1_qwen_1.5b.gguf -n 2048 --n-gpu-layers 32 --interactive
```

