from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import DB


class AITextToDBQueryGenerator:
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_query_generator(self, user_query, db_type):
        self.populate_messages(user_query, db_type)
        self.print_response_content()

    def populate_messages(self, user_query, db_type):
        default_system_content = """You are an expert programmer that helps write queries given user imput text by the {} db type 
        """.format(db_type)

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
    ai_db_query_generator = AITextToDBQueryGenerator(0.5, 4096)

    # Example 1: Text to SQL generation
    question_content = """
    Table departments, columns = [DepartmentId, DepartmentName]
    Table students, columns = [DepartmentId, StudentId, StudentName]
    Create a {} query for all students in the Computer Science Department
    """"""
 
    """.format(DB.MYSQL.name)
    # Uncomment to run
    ai_db_query_generator.general_query_generator(question_content, DB.MYSQL.name)

    # Example 2: Text to MongoDB generation
    question_content = """
    Document departments, attributes = [DepartmentId, DepartmentName]
    Document students, attributes = [DepartmentId, StudentId, StudentName]
    [INST]
    1. Create a {} query to create departments and students documents.
    2. Create a {} query to add new records to departments and students documents.
    3. Create a {} query to bring all students in the same department.
    [/INST]
    """"""
 
    """.format(DB.MONGODB.name, DB.MONGODB.name, DB.MONGODB.name)
    # Uncomment to run
    # ai_db_query_generator.general_query_generator(question_content, DB.MONGODB.name)

    # Example 3: Text to DynamoDB generation
    question_content = """
    Table departments, attributes = [DepartmentId, DepartmentName]
    Table students, attributes = [DepartmentId, StudentId, StudentName]
    [INST]
    1. Create a {} query to create departments and students documents.
    2. Create a {} query to add new records to departments and students documents.
    3. Create a {} query to bring all students in the same department.
    [/INST]
    """"""
 
    """.format(DB.DYNAMODB.name, DB.DYNAMODB.name, DB.DYNAMODB.name)
    # Uncomment to run
    # ai_db_query_generator.general_query_generator(question_content, DB.DYNAMODB.name)


if __name__ == "__main__":
    main()
