#!/usr/bin/env python3
import json
import os

def build_storyboard():
    with open("config/brand_bible.json") as f:
        config = json.load(f)

    character = config["default_character"]["prompt_tokens"]
    voice = config["default_character"]["voice_profile"]

    scenes = [
        {
            "id": 1,
            "scene": "Opening Hook",
            "visual": f"{character}, looking directly into camera with confident posture. Background: Kigali skyline at golden hour with subtle bokeh, cinematic lighting, 85mm portrait lens.",
            "dialogue": "Rwanda's infrastructure is moving fast. We need industrial precision.",
            "duration": "7.5s"
        },
        {
            "id": 2,
            "scene": "The Solution",
            "visual": f"{character}, holding a sleek industrial tablet showing a glowing cyan ERP dashboard, background subtly showing clean factory floor.",
            "dialogue": "Meet BlockMaster OS v7.0: our vertical concrete manufacturing ERP.",
            "duration": "7.5s"
        },
        {
            "id": 3,
            "scene": "The 3-Machine Fleet",
            "visual": f"{character}, gesturing towards three identical modern hydraulic block-making machines labeled Unit 01, 02, and 03.",
            "dialogue": "We operate three high-yield hydraulic block and paver machines daily.",
            "duration": "7.5s"
        },
        {
            "id": 4,
            "scene": "Product Catalog",
            "visual": f"{character}, standing near high-density Gatafari interlocking pavers and heavy-duty foundation blocks, cinematic sharp focus.",
            "dialogue": "From commercial Gatafari pavers to heavy-duty road foundation blocks.",
            "duration": "7.5s"
        },
        {
            "id": 5,
            "scene": "Sovereign Compliance",
            "visual": f"{character}, closeup of tablet screen displaying golden RRA EBM Shield badge and verified QR code transaction.",
            "dialogue": "Every coin is accounted for with instant RRA EBM QR compliance.",
            "duration": "7.5s"
        },
        {
            "id": 6,
            "scene": "BOM & Scheduling",
            "visual": f"{character}, walking through active construction site, confident expression, sharp tailored suit.",
            "dialogue": "Real-time FIFO raw material tracking keeps our projects on schedule.",
            "duration": "7.5s"
        },
        {
            "id": 7,
            "scene": "Contractor Value",
            "visual": f"{character}, gesturing directly to camera, electric cyan and gold accent lighting framing the subject.",
            "dialogue": "Contractors and builders can rent machines or order pavers directly.",
            "duration": "7.5s"
        },
        {
            "id": 8,
            "scene": "Call to Action",
            "visual": f"{character}, professional closing pose, background showing the Imboni Gorilla logo and contact banner.",
            "dialogue": "Visit imbonigroup.rw or launch BlockMaster ERP on your mobile phone.",
            "duration": "7.5s"
        }
    ]

    print("\n🎬 ========================================================")
    print("      IMBONI VIDEOEXPRESS STUDIO — 7-GATE STORYBOARD")
    print("========================================================\n")
    print(f"Locked Character Anchor: {config['default_character']['name']}")
    print(f"Voice Profile: {voice}")
    print(f"Total Scenes: {len(scenes)} (60 Seconds Total Runtime)\n")

    for s in scenes:
        char_count = len(s['dialogue'])
        status = "✓ PASS (<90 chars)" if char_count <= 90 else "⚠ FAIL (>90 chars)"
        print(f"--- [SCENE {s['id']:02d}: {s['scene']}] ({s['duration']}) ---")
        print(f"Visual Prompt:\n{s['visual']}\n")
        print(f"Actor Script Dialogue:\n\"{s['dialogue']}\"  [{char_count} chars | {status}]\n")

    # Save output to JSON for automated tools
    with open("storyboard_output.json", "w") as out:
        json.dump(scenes, out, indent=2)
    print("✓ Saved generated storyboard to storyboard_output.json")

if __name__ == "__main__":
    build_storyboard()
