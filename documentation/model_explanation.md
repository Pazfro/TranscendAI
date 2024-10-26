# Phi-3-mini-4k-instruct
### My understanding of the model

- Phi: A family or Series of small but powerfull language models. They often focus on being smaller, faster, or more optimized for specific tasks.
- 3-mini: The model is a small, light weigh version of a larger third-generation model.
- 4k: This refers to the context length the model can handle. The model can work with up to 4,000 token in its input or output sequences.
- Instruct: Models with this suffix are fine-tuned for instruction-following tasks. These models are trained to understand and follow commands, making them suitable to performing certain actions based on user input.

#### Chosen Deploy method
##### TGI for GPU or Ollma for CPU
1. I want to run inference locally without the complexity of managing GPUs.
2. Llama is easy for local deployment.
3. lower power consumption - CPU-based inference is often more power-efficient than GPUs.
4. I also dont have a Gpu
