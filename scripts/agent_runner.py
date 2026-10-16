#!/usr/bin/env python3
import os
import json
import sys

def main():
    print("🚀 Imboni VideoExpress Multi-LLM Agent Runner")
    with open("config/brand_bible.json") as f:
        config = json.load(f)

    provider = "ChatGPT (OpenAI)" if os.getenv("OPENAI_API_KEY") else "Gemini" if os.getenv("GEMINI_API_KEY") else "None"
    print(f"Active Provider: {provider}")
    print(f"Locked Character: {config['default_character']['name']}")
    print("Ready to process storyboard prompts and execute VideoExpress automations.")

if __name__ == "__main__":
    main()
