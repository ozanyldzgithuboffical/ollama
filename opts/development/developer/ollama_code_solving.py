from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import ProgrammingLanguageSet


class CodeSolving():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_code_solver(self, programming_language, code_question_request):
        self.populate_messages(programming_language, code_question_request)
        self.print_response_content()

    def populate_messages(self, programming_language, code_question_request):
        default_language = ProgrammingLanguageSet.Python.name
        if not programming_language:
            programming_language = default_language

        self.messages = [
            {
                "role": "system",
                "content": """You are an expert programmer that helps to write {}
                            code based on the user request, with concise explanations. Don't be too verbose.
                """.format(programming_language)
            },
            {
                "role": "user",
                "content": code_question_request,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)


# Developer mode main
def main():
    code_solver = CodeSolving(0.2, 4096)
    code_solver.general_code_solver(ProgrammingLanguageSet.Java.name,
                                    "Solve KnapScak Problem for me with a example in dynamic programming language")


if __name__ == "__main__":
    main()
