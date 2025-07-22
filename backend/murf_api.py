import requests

API_KEY = "your_murf_api_key"
MURF_ENDPOINT = "https://api.murf.ai/v1/speech/generate"

def generate_voice(script, voice_id):
    response = requests.post(MURF_ENDPOINT, json={
        "voice": voice_id,
        "text": script
    }, headers={"Authorization": f"Bearer {API_KEY}"})
    
    voice_url = response.json()['voice_url']
    voice_file = "uploads/voice.mp3"
    with open(voice_file, 'wb') as f:
        f.write(requests.get(voice_url).content)

    return voice_file
