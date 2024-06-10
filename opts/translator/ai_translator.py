from langchain_community.chat_models import ChatOllama


class AIUkrainianTranslator:
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=0.8, mirostat_eta=0.8, mirostat_tau=5.0, num_ctx=3500,
                              tfs_z=2.0, top_k=100, top_p=0.5)

    def general_translator(self, user_query):
        self.populate_messages(user_query)
        self.print_response_content()

    def populate_messages(self, user_query):
        default_system_content = """You are an native Turkish human. You will translate 
        from any language to Turkish by the given user query.Only translate the sentence, do not make extra comment or 
        explanation. If user query tells, your 
        translation is not correct then try to correct it.
        """

        self.messages = [
            {
                "role": "system",
                "content": default_system_content,
            },
            {
                "role": "user",
                "content": user_query,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)


# Developer mode main
def main():
    ai_ukranian = AIUkrainianTranslator(0.5, 100)

    # Example 1: Writing article about a sport topic with realistic expression by the given event
    translation_sentence = """Перевірте налаштування мережі: переконайтеся, що ваш телефон налаштований на правильну мережу. Це можна зробити в налаштуваннях телефону в розділі "Мережа і з'єднання".
    """
    #Uncomment to run
    ai_ukranian.general_translator(translation_sentence)


if __name__ == "__main__":
    main()
