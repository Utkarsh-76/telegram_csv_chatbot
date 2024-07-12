# Telegram CSV Chatbot

Create a Telegram chatbot that get answers from a csv(structured data). Chatbot for structured data

## 1. Clone the repo:

```bash
git clone https://github.com/Utkarsh-76/contract_parse_fastapi.git
```

## 2. Install packages from requirements.txt:

```bash
pip3 install -r requirements.txt
```

## 3. Setup database:

Setup a Postgres database in local and update the details in "psycopg2.connect".

## 4. Run the application

```bash
python3 tel.py
```

## Functionality

- Telegram User Interface for chat
- Upload csv to the interface
- Ask any question related to the csv

## Technical Highlights

- Library used for the telegram bot: python_telegram_bot
- Database: Postgres
- Azure open AI GPT 4 API integration for LLM

## Data flow
#### Data upload
1. Bot asks the user to upload a csv and user uploads a csv
2. A table is created in the database with 1st row of csv as column names. All the columns are saved as VARCHAR.
#### Querying the bot
1. User asks the question to the bot.
2. We give this question plus the table schema plus first 5 rows of the table in the prompt to the OpenAI API and ask for an sql query.
3. We run the query on the database. If there is not error we return the result but If we get an error we go to next step.
4. Attach the SQL query and the error to our previously generated prompt and ask GPT-4 to correct the SQL query. Repeat step 3 and 4 for a max of 4 times and return the result.

## Support

Use [this link](https://calendly.com/agarwal-ut76/30min) if you need any support for this repo or AI in general
