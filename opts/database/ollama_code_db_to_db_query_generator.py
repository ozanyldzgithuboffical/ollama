from langchain_community.chat_models import ChatOllama

from opts.common.options_enum_set import DB


class AIDBToDBQueryGenerator():
    llm = None
    messages = None

    def __init__(self, temperature, num_ctx):
        self.llm = ChatOllama(model="llama3", temperature=temperature, num_ctx=num_ctx)

    def general_query_generator(self, user_query, source_db_type, target_db_type):
        self.populate_messages(user_query, source_db_type, target_db_type)
        self.print_response_content()

    def populate_messages(self, user_query, source_db_type, target_db_type):
        default_system_content = """You are an expert programmer that helps convert queries from {} query language {} query language by
        given user input query 
        """.format(source_db_type, target_db_type)

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
    ai_db_query_generator = AIDBToDBQueryGenerator(0.5, 4096)

    # Example 1: DynamoDB dialect to SQL dialect generation
    question_content = """
    [INST]
    Definition: Convert Source Query to Target MYSQL database type query language dialect
    Source Query:
    // Create students table
    aws dynamodb create-table --table-name students \
    --attribute-definition "DepartmentId=s", "StudentId=s", "StudentName=S" \
    --key-schema '{"DepartmentId": {"KeyType": "HASH"}, "StudentId": {"KeyType": "RANGE"}}' \
    --provisioned-throughput "ReadCapacityUnits=1, WriteCapacityUnits=1"
    """"""
    [/INST]
    """
    # Uncomment to run
    ai_db_query_generator.general_query_generator(question_content, DB.DYNAMODB.name, DB.MYSQL.name)

    # Example 2: MYSQL dialect to MONGODB dialect generation
    question_content = """
    [INST]
    Definition: Convert Source Query to Target MongoDB database type query language dialect
    Source Query:
    // Number the Rows in a Result Set The following query creates a report where each row has a position value:
    SELECT employee_id, last_name, first_name, salary,
    ROW_NUMBER() OVER (ORDER BY employee_id) as ranking_position
    FROM employee
    """"""
    [/INST]
    """
    # Uncomment to run
    # ai_db_query_generator.general_query_generator(question_content, DB.MYSQL.name, DB.MONGODB.name)

    # Example 3: MYSQL dialect to GCP Big Table dialect generation
    question_content = """
    [INST]
    Definition: Convert Source Query to Target GCP Big Table database type query language dialect
    Source Query:
    // Number the Rows in a Result Set The following query creates a report where each row has a position value:
    SELECT employee_id, last_name, first_name, salary,
    ROW_NUMBER() OVER (ORDER BY employee_id) as ranking_position
    FROM employee
    """"""
    [/INST]
    """
    # Uncomment to run
    # ai_db_query_generator.general_query_generator(question_content, DB.MYSQL.name, DB.GCP_BIGTABLE.name)


if __name__ == "__main__":
    main()
