import openai
from api_keys import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def extract_shorts(captions):
    chunks = divide_captions_into_chunks(captions)
    ratings = []

    for chunk in chunks:
        text = ' '.join([caption['text'] for caption in chunk])
        rating = analyze_captions(text)
        start_time = chunk[0]['start']
        end_time = chunk[-1]['start'] + chunk[-1]['duration']
        ratings.append((rating, start_time, end_time))

    # Select the top-rated chunks
    top_shorts = sorted(ratings, reverse=True)[:3]
    timestamps = [(start_time, end_time) for _, start_time, end_time in top_shorts]
    return timestamps


def divide_captions_into_chunks(captions):
    chunks = []
    current_chunk = []
    current_time = 0
    current_tokens = 0
    MAX_TOKENS = 2048

    for caption in captions:
        caption_tokens = len(caption['text'].split())
        if current_tokens + caption_tokens > MAX_TOKENS or current_time + caption['duration'] > 15:
            chunks.append(current_chunk)
            current_chunk = [caption]
            current_time = caption['duration']
            current_tokens = caption_tokens
        else:
            current_chunk.append(caption)
            current_time += caption['duration']
            current_tokens += caption_tokens

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def analyze_captions(text):
    conversation = [
        {"role": "system",
         "content": "You are a helpful assistant that analyzes video transcripts to identify the best parts for creating YouTube shorts."},
        {"role": "user",
         "content": f"I want to create YouTube shorts from a single video. Analyze the following text and tell me if it would make a good short: {text}"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    # Extract rating from response. You will need to define logic here to extract a rating from the response message
    # The following is just an example and may not work as expected
    rating = len(response['choices'][0]['message']['content'])
    return rating
# def analyze_captions(chunk):
#     text = ' '.join([caption['text'] for caption in chunk])
#     conversation = [
#         {"role": "system",
#          "content": "You are a helpful assistant that analyzes video transcripts to identify the best parts for creating YouTube shorts."},
#         {"role": "user",
#          "content": f"I want to create YouTube shorts from a single video. Analyze the following text and tell me if it would make a good short: {text}"},
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=conversation
#     )
#     start_time = chunk[0]['start']
#     end_time = chunk[-1]['start'] + chunk[-1]['duration']
#     return start_time, end_time


def generate_youtube_link(video_id, start_time, end_time):
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    link_with_time = f"{base_url}&t={round(start_time)}s"
    return link_with_time
# f"https://www.youtube.com/watch?v={video_id}&t={start_time}s"
