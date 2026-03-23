from highrise import BaseBot
from highrise.models import SessionMetadata, User
from stream import play_song

class StarlightSnugglesBot(BaseBot):

    def __init__(self):
        super().__init__()
        self.mods = {"YOUR_USERNAME"}

    async def on_start(self, session_metadata: SessionMetadata):
        await self.send_chat("🌙 Starlight radio is live!")

    async def on_chat(self, user: User, message: str):
        msg = message.lower()

        # 🎧 Play song
        if msg.startswith("!play"):
            url = message[6:]

            if url:
                play_song(url)
                await self.send_chat(f"🎶 streaming now: {url}")
            else:
                await self.send_chat("🎧 send a valid link")

        # ⏭️ Skip (mods only)
        elif msg == "!skip":
            if user.username in self.mods:
                play_song("")  # stops current
                await self.send_chat("⏭️ skipped")
            else:
                await self.send_chat("🚫 mods only")

        # 📻 Radio link
        elif msg == "!radio":
            await self.send_chat("📻 https://your-app.up.railway.app/stream")
