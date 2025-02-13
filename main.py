import asyncio
from leave_management import LeaveManagementSystem
from ai_handler import GeminiAIHandler


async def main():
    ai_handler = GeminiAIHandler()
    lms = LeaveManagementSystem(ai_handler)

    print("Enter your username (alice, bob, charlie):")
    username = input("> ").lower()

    while True:
        query = input(
            "\nWhat would you like to do? (or type 'exit' to quit)\n> ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break

        response = await lms.process_query(username, query)
        print("\n" + response)

if __name__ == "__main__":
    asyncio.run(main())
