from langchain_community.chat_models import ChatOllama
from opts.common.options_enum_set import ProgrammingLanguageSet, TestTypes


class AITestWriter():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_test_writer(self, programming_language, test_request, test_type, coverage_rate):
        self.populate_messages(programming_language, test_request, test_type, coverage_rate)
        self.print_response_content()

    def populate_messages(self, programming_language, test_request, test_type, coverage_rate):
        default_language = ProgrammingLanguageSet.Python.name

        if not programming_language:
            programming_language = default_language

        default_system_content = """You are an expert programmer that helps write {} test or tests with {} code language. 
        Add single line comment at the top of each test. In end all business logic should be covered with written test or tests.
        The coverage must be at least % {}
        """.format(test_type, programming_language, coverage_rate)

        self.messages = [
            {
                "role": "system",
                "content": default_system_content,
            },
            {
                "role": "user",
                "content": test_request,
            }
        ]

    def print_response_content(self):
        for chunks in self.llm.stream(self.messages):
            print(chunks.content, end="", flush=True)


# Developer mode main
def main():
    ai_test_writer = AITestWriter(0.5, 4096)

    # Example 1: Writing Unit Test/s for given problem and its implementation
    # You can select a technology compatible with your selected programming lang. Such as JUnit for Java
    tech_preference = None
    question_content = """[INST] Your task is to write test/s to check the correctness that solves a programming problem.
    You must write the comment "#Test case n:" on a separate line directly above each assert statement, 
    where n represents the test case number, starting from 1 and increasing by one for each subsequent test case. 
    Problem: The following snippet filters odd numbers and implementation below:
    List oddNumbers = new ArrayList<>();
    for (Integer number : Arrays.asList(1, 2, 3, 4, 5, 6)) {
        if (number % 2 != 0) {
            oddNumbers.add(number);
        }
    }
    [/INST] 
    """
    # Uncomment and Run
    ai_test_writer.general_test_writer(ProgrammingLanguageSet.Java.name, TestTypes.Unit.name, question_content , 95)

    # Example 2: Writing Integration Test/s for given problem or its implementation
    question_content = """[INST] Your task is to write Integration test/s to check the correctness that solves a programming problem.
    You must write the comment "#Test case n:" on a separate line directly above each assert statement, 
    where n represents the test case number, starting from 1 and increasing by one for each subsequent test case. 
    Implementation: 
    @RestController
    public class EmployeeController 
    {
        @Autowired
        private EmployeeRepository employeeRepository;
    
        @GetMapping(path="/employees", produces = "application/json")
        public Employees getEmployees() 
        {
        Employees response = new Employees();
        ArrayList<Employee> list = new ArrayList<>();
        employeeRepository.findAll().forEach(e -> list.add(e));
        response.setEmployeeList(list);
            return response;
        }
        [/INST] 
    """
    # Uncomment and Run
    # ai_test_writer.general_test_writer(ProgrammingLanguageSet.Java.name, TestTypes.Integration.name, question_content , 95)

    # Example 3: Writing Smoke Test/s for given problem or its implementation
    question_content = """[INST] Your task is to write test/s to check the correctness that solves a programming problem.
    You must write the comment "#Test case n:" on a separate line directly above each assert statement, 
    where n represents the test case number, starting from 1 and increasing by one for each subsequent test case. 
    Problem Definition: Writing {} tests for a rest controller EmployeeController written by Flask connecting to GCP Big Table 
    to retrieve timeseries data.
    """.format(TestTypes.E2E.name)
    # Uncomment and Run
    # ai_test_writer.general_test_writer(ProgrammingLanguageSet.Python.name, TestTypes.E2E.name, question_content, 95)


if __name__ == "__main__":
    main()
