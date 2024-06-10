from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class TextPromptingCities():
    prompt = "Complete the sentence. You are the most beatutiful "
    llm = None

    def __init__(self):
        self.llm = Ollama(model="llama3", temperature=0.9)

    def find_cities_of_a_country(self, country_name):
        country_name = {"country_name": country_name}
        prompt = ChatPromptTemplate.from_template("Tell me top 10 cities of country : {country_name}")
        # using LangChain Expressive Language chain syntax
        chain = prompt | self.llm | StrOutputParser()

        # printing the cities
        for chunks in chain.stream(country_name):
            print(chunks, end="", flush=True)


def main():
    text_prompting = TextPromptingCities()
    text_prompting.find_cities_of_a_country("Turkey")


if __name__ == "__main__":
    main()
