# Sentiment Analysis using Flair

This Python script performs sentiment analysis on a set of tweets using the Flair library. The sentiment analysis model is trained to classify the sentiment of the provided text into positive, negative, or neutral.

## Usage

1. Install Dependencies

Make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

2. Set Up Twitter API Credentials

Create a Twitter Developer account and obtain the API key, API key secret, Bearer token, Access token, and Access token secret. Set these credentials as environment variables in a .env file in the same directory as the script. Example .env file:

```bash
API_Key = your_api_key
API_Key_Secret = your_api_key_secret
Bearer_Token = your_bearer_token
Access_Token = your_access_token
Access_Token_Secret = your_access_token_secret
```

3. Choose Data Source

The script provides two options for the source of tweets:

- Twitter API v2: Uncomment the relevant code block to use the Twitter API v2. Note that access to Twitter API v2 may require payment.
- Hardcoded Tweets: If you haven't paid for the Twitter developer account, a set of hardcoded tweets is provided for demonstration purposes.

4. Run the Script

Execute the script using the following command:

```bash
python app.py
```

## Important Note
The hardcoded tweets are used as a fallback due to the potential cost associated with accessing Twitter API v2 for real-time tweet data. If you have the resources, consider using the Twitter API v2 by uncommenting the relevant code block and handling the necessary pre-processing steps.
