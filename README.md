# Imboni VideoExpress Studio (v7.3)
### Autonomous 7-Gate Multi-Agent Video Engine for BlockMaster Rwanda

Automated video production studio converting raw operational logs, BOM yields, and client delivery manifests into 60-second vertical social videos (9:16) with lipsync dialogue under 90 characters per chunk.

## Pipeline Architecture
- **Gate 0-1**: Operational Prompt Ingestion & Validation
- **Gate 2**: Multi-LLM Storyboard Generation (OpenAI ChatGPT & Google Gemini)
- **Gate 3-4**: Audio & CloneVoice Synthesis (<90 chars per scene)
- **Gate 5-6**: VideoExpress Browser Automation & Final Composition

## Quickstart
```bash
python3 scripts/generate_storyboard.py
```

**Classification**: IMBONI PRIME INNOVATIONS // KIGALI, RWANDA // 2026
