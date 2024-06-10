from enum import Enum

from langchain_community.chat_models import ChatOllama


class OllamaConfigurationEnum(Enum):
    temperature = 1
    num_ctx = 2


class OllamaConfiguration:
    num_ctx = None
    temperature = None
    mirostat_eta = None
    mirostat_tau = None
    repeat_penalty = None
    tfs_z = None
    top_k = None
    top_p = None

    def __init__(self, temperature=0.1, num_ctx=4096, mirostat_eta=0.1, mirostat_tau=5.0, repeat_penalty=1.1, tfs_z=1.0,
                 top_k=40, top_p=0.9):
        self.temperature = temperature
        self.num_ctx = num_ctx
        self.mirostat_eta = mirostat_eta
        self.mirostat_tau = mirostat_tau
        self.repeat_penalty = repeat_penalty
        self.tfs_z = tfs_z
        self.top_k = top_k
        self.top_p = top_p

    def create_chat_llama(self):
        return ChatOllama(model="llama3", temperature=self.temperature, num_ctx=self.num_ctx,
                          mirostat_eta=self.mirostat_eta, mirostat_tau=self.mirostat_tau,
                          repeat_penalty=self.repeat_penalty, tfs_z=self.tfs_z, top_k=self.top_k, top_p=self.top_p)

    def get_ollama_model_default_config_settings(self):
        return {
            "temperature": self.temperature,
            "num_ctx": self.num_ctx,
            "mirostat_eta": self.mirostat_eta,
            "mirostat_tau": self.mirostat_tau,
            "repeat_penalty": self.repeat_penalty,
            "tfs_z": self.tfs_z,
            "top_k": self.top_k,
            "top_p": self.top_p,
        }
