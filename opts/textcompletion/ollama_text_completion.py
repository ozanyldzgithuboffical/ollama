from langchain_community.llms import Ollama


class TexCompletion():
    prompt = "Complete the sentence. You are the most beatutiful "
    llm = None

    def __init__(self):
        self.llm = Ollama(model="llama3", temperature=0.9, mirostat_eta=0.3, mirostat_tau=7.0, num_ctx=3500,
                          repeat_penalty=1.1, tfs_z=2.0, top_k=100, top_p=0.95)

    def test_raw_text_completion(self):
        for chunks in self.llm.stream(self.prompt):
            print(chunks, end="", flush=True)


def main():
    text_completion = TexCompletion()
    text_completion.test_raw_text_completion()


if __name__ == "__main__":
    main()
