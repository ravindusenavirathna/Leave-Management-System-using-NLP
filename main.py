import asyncio
from leave_management import LeaveManagementSystem
from ai_handler import GeminiAIHandler


async def main():
    ai_handler = GeminiAIHandler()
    lms = LeaveManagementSystem(ai_handler)

    print("\nWelcome to the Leave Management System!")
    print("Enter your username (alice, bob, or charlie):")

    while True:
        username = input("> ").lower()
        if username in lms.employees:
            break
        print("Invalid username. Please try again with alice, bob, or charlie:")

    print(f"\nWelcome {username.capitalize()}!")
    print("\nYou can:")
    print("- Check your leave balance")
    print("- Request leave")
    print("- Cancel leave")
    print("- View leave history")
    print("\nJust type your request in natural language.")

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
