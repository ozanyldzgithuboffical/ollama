**Warning: All rights are reserved and you can not use this code to produce the financial earning products**
**Please check official Meta LLAMA website and for financial earning related products follow their instructions**
**This repository is just for educational purpose to be aware of what kind of things you can do with the help of Generative AI and NLP**

# Project Prerequisites and Recommended IDEA
- You can use PyCharm Community Edition IDEA
- You should install latest Python, PiP and Homebrew ready.
- You should install and login to your POSTMAN account to send example requests.
- Once you open the project in IDEA , you can check the files imports section and install the latest missing dependencies.
  
# LLMA 3 - 8B Instruct Model Installation and Model Prerequisites 
- Published March 2023.
## Meta LLAMA 3 Models Available
- LLAMA 8B
- LLAMA 8B-Instruct (Fine-Tuned)
- LLAMA 70B
- LLAMA 70B-Instruct (Fine-Tuned)
  
## Hardware Prerequisites

### CPU
- 4 cores CPU running for smaller models
- 8 cores CPU running for 13B or greater models.
- GPU is optional but increases the performance drastically. You can check out integrating CUDA Nvidia GPU accelarator.

### RAM
- At least 8GB of RAM to run 7B models.
- 16 GB of RAM for 13B models
- 32 GB of RAM for 33B or greater models.

### DISK CAPACITY
- At least 12 GB of disk space to install the Meta LLAMA 3 model.
- Additional disk space maybe needed if more models are installed.

## INSTALLATION
- Go to page to download the OLLAMA Model : https://ollama.com/download
- For Mac OS , Windows  and Linux there are installation options separately.
- Once the installation is done, you will be able to see OLLAMA icon in task bar.
- OLLAMA server is up and listens 11434 with localhost.  http://localhost:11434/
- Open a terminal and run llama-3 model locally : '''ollama run llama3''' which refers to ollama 8B
- If you need 70B model to run, then you need to run: '''ollama run llama3:70b'''
- For the pretrained (fine-tuned) base variables you need to run: '''ollama run llama3:text''' for 8B and '''ollama run llama:70b-text'''
- Once model is downloaded model is ready to use and you can list running model : '''ollama list'''
- If an upgraded model of llama3 is released you can run : '''ollama pull llama3''' or its variants mentioned upward.
- If you want to remove the model you can run '''ollama rm llama3''' or its variants mentioned upward.

# Project Structure:
- opts: Having multiple sub use-cases then you can run from terminal cli.
- app: Example rest api written with Python Flask framework and includes example use case related to being a AI developer for cases such as code evaluation, test writer etc.
- service: It includes the logic for the incoming requests from app.

# How to Run the Service:
- You need to run , app/developer_api.py minor microservice if you want to send requests for some examples over Postman.
- You can run any of the python files under opts folder to try the results for different uses cases with OLLAMA to see the results over internal terminal.
- Note That: For the first run it can take a little bit more time to show the results around 15-20 seconds but later it will be shorter with caching the requests.
- This is just an educational resource, so it is quite normal that you need to have your own infrastructure enriched with GPU and super computer clusters to make a real project.
    
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
