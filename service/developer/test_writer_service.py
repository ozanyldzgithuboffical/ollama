from opts.common.options_enum_set import ProgrammingLanguageSet, TestTypes
from service.config.ollama_settings import OllamaConfiguration


class OllamaTestWriter:
    llm = None
    messages = None

    def __init__(self, temperature=0.5, num_ctx=2048):
        ollama_developer_settings = OllamaConfiguration(temperature, num_ctx)
        self.llm = ollama_developer_settings.create_chat_llama()

    def general_test_writer(self, code_question_request, test_instruction, is_verbose):
        self.populate_messages_tester(code_question_request, test_instruction, is_verbose)
        return self.return_content_response()

    def populate_messages_tester(self, code_question_request, test_instruction, is_verbose):
        default_verbose = "Don't Be verbose."
        if not is_verbose:
            default_verbose = "Be verbose."

        self.messages = [
            {
                "role": "system",
                "content": """You are an very expert test and quality assurance developer for any programming language 
                that helps to write test cases by requested test type or types and code logic given in user query such 
                as {} , {}, {}, {}, {} , {} and {} tests.{}.Please consider the code logic strongly be related to test 
                cases and requested test type in test instruction in user query. Be careful is there any bad or 
                unethical word. If you feel given code logic and requested test type or types contain not related to 
                programming then do not give information. Be careful test instruction must be related to test programming,
                otherwise do not answer.
                """.format(TestTypes.Unit, TestTypes.Integration, TestTypes.E2E, TestTypes.Smoke, TestTypes.Functional,
                           TestTypes.Regression, TestTypes.Acceptance, default_verbose)
            },
            {
                "role": "user",
                "content": """Test Instruction: {} and Code Logic: {}""".format(test_instruction, code_question_request)
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
