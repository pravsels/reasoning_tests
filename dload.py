from huggingface_hub import snapshot_download

snapshot_download(
  repo_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
  local_dir = "llama.cpp/DeepSeek_R1_QWEN_1.5B"
)
