# Leave Management System

## Overview

The Leave Management System is an AI-powered tool that allows employees to check their leave balance, request leave, cancel leave, and view their leave history using natural language queries. The system utilizes Gemini AI for query processing and understanding.

## Features

- **Check leave balance**: View remaining leave days for different leave types.
- **Request leave**: Submit leave requests, including leave type, duration, and start date.
- **Cancel leave**: Cancel an approved leave request.
- **View leave history**: Retrieve details of past leave requests.

## Technologies Used

- **Python** (FastAPI for backend processing)
- **Google Gemini AI** (Natural language processing)
- **dotenv** (Environment variable management)
- **Asyncio** (Asynchronous processing)

## Prerequisites

Before running the project, ensure you have:

- Python 3.8 or higher installed.
- An API key for Google Gemini AI.
- Required dependencies installed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/leave-management.git
   cd leave-management
   ```
2. Create a `.env` file in the project root and add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

Run the application using:

```bash
python main.py
```

## Usage

1. Start the application.
2. Enter your username (alice, bob, or charlie).
3. Input natural language queries such as:
   - "How many sick leaves do I have left?"
   - "I want to take annual leave for 3 days starting from 2024-02-15."
   - "Cancel my sick leave for 2024-02-10."
   - "Show my leave history."
4. The system will process your request and respond accordingly.

## Example Queries

- "Check my annual leave balance."
- "Request 5 days of sick leave starting from March 10, 2024."
- "Cancel my leave from April 5, 2024."
- "Show my leave history."
