from agent import SQLAgent

def main():
    agent = SQLAgent()

    question = input("Ask your question: ")

    result = agent.run(question)

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    main()
