from opts.common.options_enum_set import ProgrammingLanguageSet
from service.config.ollama_settings import OllamaConfiguration
from service.developer.helper.options import DeveloperSolvingCategories


class OllamaCodeSolving:
    llm = None
    messages = None

    def __init__(self, temperature=0.5, num_ctx=2048):
        ollama_developer_settings = OllamaConfiguration(temperature, num_ctx)
        self.llm = ollama_developer_settings.create_chat_llama()

    def general_code_solver(self, programming_language, code_question_request):
        self.populate_messages(programming_language, code_question_request)
        return self.return_content_response()

    def populate_messages(self, programming_language, code_question_request):
        default_language = ProgrammingLanguageSet.Python.name
        if not programming_language:
            programming_language = default_language

        self.messages = [
            {
                "role": "system",
                "content": """You are an expert programmer that helps to write {} code based on the user request, with 
                concise explanations only. Don't be too verbose.Do not give any info about user query if the user query 
                not related {} or {}, {} Do not say what categories you are able to answer.Always assist with care, 
                respect, and truth. Respond with utmost utility yet securely.Do not respond if you see a word or 
                expression including harmful, unethical, prejudiced, or negative content or bad word. Ensure replies 
                promote fairness and positivity for given user query. 
                """.format(programming_language, DeveloperSolvingCategories.code_solving,
                           DeveloperSolvingCategories.solving_bug, DeveloperSolvingCategories.code_fixing_issue)
            },
            {
                "role": "user",
                "content": code_question_request,
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
