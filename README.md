## ChatGPT Weather Plugin using Open-Meteo API

This plugin is a simple example of how to use the Open-Meteo API to get weather data and display it in ChatGPT.

### Local Setup

1. `poetry install` to install the dependencies
2. `poetry run python uvicorn api.main:app` to run the API

### Deploying to Vercel

1. Generate a copy of `requirements.txt` from poetry pyproject.toml by running `poetry export --without-hashes -o requirements.txt`
2. Create a new project on Vercel or setup the CLI
3. Manually setup the project to Vercel UI or using the CLI by running `vercel deploy`

### Test the API to LangChain (if you still have no access to ChatGPT Plugins like me huhu)

1. Open the notebook `(chatgpt_plugins_langchain_weather_mac.ipynb)` to google colab and replace the API URL with your own API URL
