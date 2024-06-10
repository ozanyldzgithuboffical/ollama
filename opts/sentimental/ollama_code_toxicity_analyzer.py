from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import ToxicityCategory


class AISpamAnalyzer():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_toxicity_spam_analyzer(self, user_query):
        self.populate_messages(user_query)
        self.print_response_content()

    def populate_messages(self, user_query):
        default_system_content = """You are an expert user comment toxicity analyist 
        that helps to identify given user imput comment by these categories:
        {}, {} , {} , {} , {} , {} , {} , {} . Comment can enter multiple categories. 
        In the end ,  state the user comment spam or not spam. Besides, give recommendation to system
        about how to filter by given user comment.
        """.format(ToxicityCategory.Hate, ToxicityCategory.Insult,
                   ToxicityCategory.Obscene, ToxicityCategory.SevereToxic,
                   ToxicityCategory.Toxic
                   , ToxicityCategory.Sexual, ToxicityCategory.Threat, ToxicityCategory.Promotional)

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
    ai_spam_analyzer = AISpamAnalyzer(0.5, 4096)

    # Example 1: Threat and Insult Included User Comment
    user_comment_message = """
    Comment: You’re an idiot person, and I hope someone hits you!

    Analyze the toxicity and is spam status of user comment.
    """
    # Uncomment to run
    ai_spam_analyzer.general_toxicity_spam_analyzer(user_comment_message)

    # Example 2: Threat and Insult Included User Comment
    user_comment_message = """
    Comment: if you like raw talent, raw lyrics, straight real hip hop Everyone check my newest sound Dizzy X - ...

    Analyze the toxicity and is spam status of user comment.
    """
    # Uncomment to run
    # ai_spam_analyzer.general_toxicity_spam_analyzer(user_comment_message)

    # Example 3: Positive comment
    user_comment_message = """
    Comment: That was really nice restaurant. We would like to stop by again.

    Analyze the toxicity and is spam status of user comment.
    """
    # Uncomment to run
    # ai_spam_analyzer.general_toxicity_spam_analyzer(user_comment_message)


if __name__ == "__main__":
    main()
