from langchain_community.chat_models import ChatOllama
from opts.common.options_enum_set import NewspaperTopic, ExpressionType


class AINewsPaperRobotWriter:
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_newspaper_article_generator(self, user_query, newspaper_topic, expression_type):
        self.populate_messages(user_query, newspaper_topic, expression_type)
        self.print_response_content()

    def populate_messages(self, user_query, newspaper_topic, expression_type):
        default_system_content = """You are an expert and famous newspaper writer on {} field.
        For the newspaper, you will write a newspaper article based on the information 
        you are given about the topic or event in the user input. Be {} with your article.
        Do not add contact information.
        """.format(newspaper_topic, expression_type)

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
    ai_newspaper_writer_robot = AINewsPaperRobotWriter(0.5, 100)

    # Example 1: Writing article about a sport topic with realistic expression by the given event
    article_instruction = """
    [INST]
    Write a newspaper arcticle about sport event allegedly talked:
    Kylian Mbappe's name has been linked with Real Madrid.
    [/INST]
    """
    #Uncomment to run
    #ai_newspaper_writer_robot.general_newspaper_article_generator(article_instruction, NewspaperTopic.Sports, ExpressionType.Realistic)

    # Example 2: Writing an article about Louis Vuitton new hotel in Paris
    article_instruction = """
    [INST]
    Write a newspaper arcticle about fashion icon brand Louis Vuitton:
    Louis Vuitton opens a new hotel in Paris Shanzelize street.
    [/INST]
    """
    #Uncomment to run
    ai_newspaper_writer_robot.general_newspaper_article_generator(article_instruction, NewspaperTopic.Fashion,
                                                                  ExpressionType.Realistic)


if __name__ == "__main__":
    main()
