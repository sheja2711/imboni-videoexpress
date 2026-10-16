# Verified DOM Selectors & UI Interactions

- Gallery Toggle: `input[type="checkbox"][name="public_gallery"]` -> Must be set to FALSE.
- Create Button: `button[data-testid="create-video-btn"]`
- Actor Script Modal: `div[role="dialog"] textarea[name="actor_dialog"]`
- Voice Selector: `select[name="voice_profile"]` -> Select matched CloneVoice profile.
- Timeline Track 0: `#editor-timeline-track-video`
- Timeline Track 1: `#editor-timeline-track-audio`
- Export Button: `button#btn-export-1080p`
- Polling Interval: Check render state every 20-30s. Never refresh the browser window during render.
