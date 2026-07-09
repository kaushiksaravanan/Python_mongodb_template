# Python_mongodb_template

A small Python starter I copy into projects that need to talk to MongoDB Atlas.

## Setup

```bash
git clone https://github.com/kaushiksaravanan/Python_mongodb_template.git
cd Python_mongodb_template
pip install pymongo requests python-dotenv
cp .env.example .env
```

Then open `.env` and fill in your real MongoDB connection string.

## Environment variables

- `MONGODB_URI`: Full Atlas connection string in the form `mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority`. Never commit the real value; `.env` is gitignored.

## Run

```bash
python main.py
```

## What it does

- Connects to a MongoDB Atlas cluster using the URI from the environment.
- Opens a database and collection, then does whatever work the script is set up for (the checked-in `main.py` is a small example that generates random ids and probes a URL pattern).
- Serves as scaffolding I fork when a new project needs pymongo wired up quickly.

Personal template, not production code. Fork it, rip out the example loop in `main.py`, and drop in your own logic.
