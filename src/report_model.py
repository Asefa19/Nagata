from llama_cpp import Llama

def report_Model():
  model_gguf="/Nagata/model/astrollama-3-8b-chat_summary.Q8_0.gguf"

  # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
  llm = Llama(
    model_path=model_gguf,  # Download the model file first
    n_ctx=1024,  # The max sequence length to use - note that longer sequence lengths require much more resources
    n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
    n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
  )

  # Simple inference example
  output = llm(
    "<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>", # Prompt
    max_tokens=512,  # Generate up to 512 tokens
    stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
    echo=True        # Whether to echo the prompt
  )

  # Chat Completion API

  llm = Llama(model_path=model_gguf, chat_format="llama-2")  # Set chat_format according to the model you are using
  response = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are a report writer and reviewer."},
          {
              "role": "user",
              "content": "Can you write a 2 paragraph report on the sun's atmosphere?" 
          }
      ]
  )

  print(response)