from langchain_community.chat_models import ChatOllama


class AIUserCommentSentimentalAnalyzer():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_user_review_analyzer(self, user_query):
        self.populate_messages(user_query)
        self.print_response_content()

    def populate_messages(self, user_query):
        default_system_content = """You are an expert e-commerce sales manager who analyzes the user comments 
        whether the given user comment is positive or negative or not by the given user comment input.
        If user comment is negative, generate some recommendations for given product to make customer happy.
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
    ai_user_review_analyzer = AIUserCommentSentimentalAnalyzer(0.5, 4096)

    # Example 1: Positive user comment about a product
    user_review = """
    Product review by user comment: 
    This smartphone is amazing! Super-fast delivery too!"Response: Thank you for your kind words! 
    We're delighted to hear that you're happy with your new smartphone and our speedy delivery service.
    
    Analyze the comment whether customer is happy or not.
    """
    # Uncomment to run
    ai_user_review_analyzer.general_user_review_analyzer(user_review)

    # Example 2: Negative user comment about a product
    user_review = """
    Product review by user comment: 
    This electronic item stopped working after a month of use."Response: We're sorry to hear about the issue with your purchase. 
    Please contact our support team, and we'll assist with warranty options or repairs.
    
    Analyze the comment whether customer is happy or not.
    """
    # Uncomment to run
    # ai_user_review_analyzer.general_user_review_analyzer(user_review)


if __name__ == "__main__":
    main()
