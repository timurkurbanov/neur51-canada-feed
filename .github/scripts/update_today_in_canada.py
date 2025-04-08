# .github/scripts/update_today_in_canada.py

import datetime
import json
from openai import OpenAI
from pathlib import Path

client = OpenAI()

def generate_ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Canadian historian and poetic brand voice."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()

# Get today’s date
today = datetime.datetime.now().strftime("%B %d")

# AI prompts
history_prompt = f"Give me a short historical fact that happened in Canadian history on {today}. Max 25 words."
birthday_prompt = f"Name a famous Canadian born on {today}, with a short one-line fact about them."
energy_prompt = "Write a poetic line about Canadian spirit using nature metaphors. One sentence."

# Generate responses
history = generate_ai_response(history_prompt)
birthday = generate_ai_response(birthday_prompt)
energy = generate_ai_response(energy_prompt)

# Example product
product = {
    "name": "Deep North Black Hoodie",
    "link": "/products/deep-north-black-hoodie",
    "description": "Made for days when you don’t raise your voice—but everyone listens."
}

# Build final JSON
output = {
    "date": today,
    "history": history,
    "birthday": birthday,
    "energy": energy,
    "product": product
}

# Save to JSON
Path("today-in-canada.json").write_text(json.dumps(output, indent=2))
