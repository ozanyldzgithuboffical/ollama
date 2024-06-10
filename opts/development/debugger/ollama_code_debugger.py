from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import TaskType


class CodeDebugger():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_code_debugger(self, programming_language, code_review_request, task_type):
        self.populate_messages(programming_language, code_review_request, task_type)
        self.print_response_content()

    def populate_messages(self, programming_language, code_review_request, task_type):
        default_language = "Python"
        default_task_type = "bugs"

        if not programming_language:
            programming_language = default_language

        if not task_type:
            task_type = default_task_type

        default_system_content = """You are an expert programmer that helps to review {} code for  {}  
        based on the user request, with concise explanations. Don't be too verbose.
        """.format(programming_language, task_type)

        if task_type == "code_quality":
            default_system_content = """You are an expert programmer that helps to review {} code in terms of code quality  
            based on the user request, with concise explanations and code change suggestions if needed. Don't be too verbose.
            """.format(programming_language)

        self.messages = [
            {
                "role": "system",
                "content": default_system_content,
            },
            {
                "role": "user",
                "content": code_review_request,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)


# Developer mode main
def main():
    code_debugger = CodeDebugger(0.2, 4096)
    # Bug Solver Example : 
    task_type = TaskType.bugs.name
    question_content = """ Where is the bug in the code below ?
    methods = []                       
    for i in range(10):                        
         methods.append(lambda x: x + i)        

    print methods[0](10)  
    """
    # Uncomment to run
    code_debugger.general_code_debugger("Python", question_content, task_type)

    # Improve Code Quality
    task_type = TaskType.code_quality.name
    question_content = """ Write me a better code quality code for snippet below :
    def func_x(num):
    if num == 1:
        return a()
    elif num == 2:
        return b()
    elif num == 3:
        return c()
    elif num == 4:
        return d()
    elif num == 5:
        return e()
    """
    # Uncomment to run
    # code_debugger.general_code_debugger("Python", question_content, task_type)


if __name__ == "__main__":
    main()
