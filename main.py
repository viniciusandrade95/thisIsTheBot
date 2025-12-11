"""Entry point for the brow designer chatbot."""
from conversation import ConversationManager


def main() -> None:
    manager = ConversationManager()
    print("BrowBot ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Bot: Bye!")
            break
        response = manager.process_input(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
