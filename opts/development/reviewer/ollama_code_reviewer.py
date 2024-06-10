from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import ProgrammingLanguageSet, ApprovalType


class CodeReviewer():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_code_reviewer(self, programming_language, code_review_request):
        self.populate_messages(programming_language, code_review_request)
        self.print_response_content()

    def populate_messages(self, programming_language, code_review_request):
        default_language = ProgrammingLanguageSet.Python.name

        if not programming_language:
            programming_language = default_language

        default_system_content = """You are an expert programmer that helps to review 
        {} code logic for bugs and general review. Do your analysis statement only for lines need improvement.
        If line is correct and does not need suggestion do not prompt that line analysis in response.
        If code logic correct completely and code is in good code quality , 
        then state code approval status {} in the end. Otherwise, if you have prompt like in stead of using  or suggestion
        or if you see a bug  then  state recommended change by the line number prefixed as Line in user request 
        and state code approval status {} in the end.
        """.format(programming_language, ApprovalType.Approved.name, ApprovalType.Needs_Change.name)

        self.messages = [
            {
                "role": "user",
                "role": "system",
                "content": default_system_content,
            },
            {
                "content": code_review_request,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)


# Developer mode main
def main():
    code_debugger = CodeReviewer(0.2, 4096)
    # Code Reviewer Example 1: Approved Code
    question_content = """ Could you please review the code below ? Implemented Logic: The following snippet filters odd numbers.
    Line 1: List oddNumbers = new ArrayList<>();
    Line 2: for (Integer number : Arrays.asList(1, 2, 3, 4, 5, 6)) {
    Line 3:     if (number % 2 != 0) {
    Line 4:         oddNumbers.add(number);
    Line 5:     }
    Line 6: } 
    """
    # Uncomment to run
    code_debugger.general_code_reviewer(ProgrammingLanguageSet.Java.name, question_content)

    # Code Reviewer Example 2: Needs Change Code
    question_content = """ Could you please review the code below ? Implemented Logic: The following snippet filters odd numbers.
    Line 1: List oddNumbers = new ArrayList<>();
    Line 2: for (Integer number : Arrays.asList(1, 2, 3, 4, 5, 6)) {
    Line 3:     if (number % 5 != 0) {
    Line 4:         oddNumbers.add(number) + 1;
    Line 5:     }
    Line 6: } 
    """
    # Uncomment to run the example
    # code_debugger.general_code_reviewer(ProgrammingLanguageSet.Java.name, question_content)


if __name__ == "__main__":
    main()
