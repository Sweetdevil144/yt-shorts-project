# YouTube Shorts Creator

## Overview
This project aims to analyze YouTube video captions to find amusing parts and create YouTube shorts from them. By fetching the subtitles of a specific video and applying sentiment analysis, it automatically detects the sections with positive sentiments and converts them into short YouTube video URLs.

## Requirements
To run the script, you will need the following libraries and tools:

- **Python 3.x**: The code is written in Python.
- **OpenAI API**: Used for sentiment analysis.
- **youtube_transcript_api**: For fetching YouTube subtitles.
- **google-api-python-client**: For YouTube Data API v3.

You can install the required Python libraries using the following command:
```bash
pip3 install -r requirements.txt
```

## Tools Used
- **YouTube Data API**: To fetch video captions.
- **OpenAI GPT-4**: To analyze the sentiment of the captions.

## Knowledge Required
Understanding the code requires a basic understanding of:
- **Python programming**: Basic programming knowledge in Python is necessary.
- **API interaction**: Familiarity with using web APIs will help in understanding how data is fetched and analyzed.
- **Sentiment analysis**: Knowledge of Natural Language Processing (NLP) and specifically sentiment analysis would be beneficial.

## How to Run
1. **Clone the Repository**: Clone the project to your local machine.
2. **Set API Keys**: Replace the placeholders in `api_keys.py` with your YouTube and OpenAI API keys.
3. **Run the Script**: Execute `main.py` to fetch video captions and create YouTube shorts.

```bash
python3 main.py
```

## Special thanks to GPT-4 for powering the sentiment analysis and to [Avijit Thawani](https://github.com/avi-jit) for his contributions to this project.
