from llama_cpp import Llama

def analysis_model(model_gguf):

    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    llm = Llama(
    model_path=model_gguf,  # Download the model file first
    n_ctx=512,  # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
    n_gpu_layers=32,         # The number of layers to offload to GPU, if you have GPU acceleration available
    chat_format="llama-2",
    verbose=False
    )
    return llm

  # # Simple inference example
  # output = llm(
  #   "<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>", # Prompt
  #   max_tokens=512,  # Generate up to 512 tokens
  #   stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  #   echo=True        # Whether to echo the prompt
  # )

