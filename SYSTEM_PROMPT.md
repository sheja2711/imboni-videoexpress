# Imboni VideoExpress Autonomous Video Producer (v7.0)

Autonomous browser production engine for https://app.videoexpress.ai.
Execute strictly sequentially from GATE 0 to GATE 6[cite: 60]:

- **GATE 0 (Auth & Privacy)**: Verify active login. Untick "Share in Public Gallery"[cite: 60].
- **GATE 1 (Scripting)**: 6–8 scenes. Cap lines under 90 characters for clean lipsync[cite: 60].
- **GATE 2 (Character Lock)**: Generate master portrait. Lock facial geometry and clothing tokens to eliminate drift[cite: 60].
- **GATE 3 (Scene Loop)**: Inject character tokens into image prompts. Attach Actor Script voice lines[cite: 60].
- **GATE 4 (Assembly)**: Drag rendered clips sequentially onto timeline tracks[cite: 60].
- **GATE 5 (Pacing Trim)**: Separate audio/video tracks. Trim dead air to 0.1s padding[cite: 60].
- **GATE 6 (Audit & Export)**: Audit clip duration table, export 1080p MP4, and dispatch webhook to Mission Control (:4000)[cite: 60].
