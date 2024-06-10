# Options OLLAMA
## Required Params
- model : Name of the model. Check out provider from official langchain site.

## Most Used Optional Params
- num_ctx : Max number of tokens. Default: 2048 , Max: 4096
- temperature : 0.0-1.0 double value. More creative when you pick near to 1.0
- mirostat_eta: Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive. (Default: 0.1)
- mirostat_tau: Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text. (Default: 5.0)
- repeat_penalty : Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient. (Default: 1.1)
- seed : Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt. (Default: 0)
- tfs_z : Tail free sampling is used to reduce the impact of less probable tokens from the output. A higher value (e.g., 2.0) will reduce the impact more, while a value of 1.0 disables this setting. (default: 1)
- top_k : Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)
- top_p : Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)
