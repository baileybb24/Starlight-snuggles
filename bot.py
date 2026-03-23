from highrise import BaseBot
from highrise.models import SessionMetadata, User
import asyncio

class StarlightSnugglesBot(BaseBot):

    def __init__(self):
        super().__init__()
        self.queue = []
        self.current_song = None
        self.mods = set()  # add usernames manually

    async def on_start(self, session_metadata: SessionMetadata):
        print("✨ Music bot online!")
        await self.send_chat("🌙 Starlight Snuggles radio is live ✨")

    async def on_chat(self, user: User, message: str):
        msg = message.lower()

        # 👑 Add mod (you can hardcode yourself)
        if user.username == "YOUR_USERNAME":
            self.mods.add(user.username)

        # 🎶 Add song
        if msg.startswith("!play"):
            song = message[6:]
            if song:
                self.queue.append(song)
                await self.send_chat(f"🎧 added to queue: {song}")
            else:
                await self.send_chat("🎶 tell me what to play")

        # 📻 Show radio URL
        elif msg == "!radio":
            await self.send_chat("📻 Radio URL: https://your-stream-url.up.railway.app/stream")

        # ⏭️ Skip (mods only)
        elif msg == "!skip":
            if user.username in self.mods:
                if self.queue:
                    self.current_song = self.queue.pop(0)
                    await self.send_chat(f"⏭️ skipped! now playing: {self.current_song}")
                else:
                    await self.send_chat("❌ queue is empty")
            else:
                await self.send_chat("🚫 mods only")

        # 📜 Queue
        elif msg == "!queue":
            if self.queue:
                q = ", ".join(self.queue[:5])
                await self.send_chat(f"🎶 queue: {q}")
            else:
                await self.send_chat("🌙 queue is empty")
