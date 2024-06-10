from opts.common.options_enum_set import ProgrammingLanguageSet
from service.config.ollama_settings import OllamaConfiguration


class OllamaCodeReviewer:
    llm = None
    messages = None

    def __init__(self, temperature=0.5, num_ctx=2048):
        ollama_developer_settings = OllamaConfiguration(temperature, num_ctx)
        self.llm = ollama_developer_settings.create_chat_llama()

    def general_code_reviewer(self, pull_request_title, code_question_request, is_verbose):
        self.populate_messages_reviewer(pull_request_title, code_question_request, is_verbose)
        return self.return_content_response()

    def populate_messages_reviewer(self, pull_request_title, code_question_request, is_verbose):
        default_language = ProgrammingLanguageSet.Python.name
        default_verbose = "Don't Be verbose."
        if not is_verbose:
            default_verbose = "Be verbose."

        self.messages = [
            {
                "role": "system",
                "content": """You are an very expert programmer that helps to review code logic of all  programming 
                languages code logic for bugs and general code review.{}.
                Please consider title is relating the code strongly and either title or code having any unrelated
                something to a programming language in meaning very strictly, otherwise do not make any comment.
                State if there is unnecessary space and do not explain if code is correct with title logic.
                After checking previous steps upward  later make, make static code analysis also, if there is something to fix state that code needs change.
                Only make comment for wrong parts you see. Be careful is there any bad or unethical word.
                """.format(default_verbose)
            },
            {
                "role": "user",
                "content": "Pull request title:" + pull_request_title + " Code:" + code_question_request,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)

    def get_default_config_settings(self):
        ollama_developer_settings_config = OllamaConfiguration()
        return ollama_developer_settings_config.get_ollama_model_default_config_settings()

    def return_content_response(self):
        response = ""
        for chunks in self.llm.stream(self.messages):
            response = response + chunks.content
        return response
