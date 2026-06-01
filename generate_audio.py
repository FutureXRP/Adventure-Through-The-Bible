import requests
import json
import base64
import sys
import os

API_KEY = "sk_1a8724ab5dd740192c4868cc8029cea9ae4e940f79edd882"
VOICE_ID = "1wg2wOjdEWKA7yQD8Kca"

def generate(story_id):
    # Load story text from stories.json
    with open('stories.json') as f:
        data = json.load(f)

    story = next((s for s in data['stories'] if s['id'] == story_id), None)
    if not story:
        print(f"Story '{story_id}' not found")
        return

    # Join all paragraphs into one block of text
    text = ' '.join(story['story'])
    print(f"Generating: {story['title']} ({len(text)} characters)")

    # Call ElevenLabs with-timestamps endpoint
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps",
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }
    )

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return

    result = response.json()

    # Save MP3
    os.makedirs('audio', exist_ok=True)
    audio_bytes = base64.b64decode(result['audio_base64'])
    mp3_path = f"audio/{story_id}.mp3"
    with open(mp3_path, 'wb') as f:
        f.write(audio_bytes)
    print(f"Saved: {mp3_path} ({len(audio_bytes):,} bytes)")

    # Save timestamps
    json_path = f"audio/{story_id}.json"
    with open(json_path, 'w') as f:
        json.dump(result['alignment'], f, indent=2)
    print(f"Saved: {json_path}")
    print(f"Words timestamped: {len(result['alignment']['characters'])}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_audio.py <story_id>")
        print("Example: python3 generate_audio.py creation")
    else:
        generate(sys.argv[1])