from highrise import BaseBot
from highrise.models import SessionMetadata, User, Position
import random

class StarlightSnugglesBot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata):
        print("✨ Starlight Snuggles is online!")

        # Optional: send message when bot starts
        await self.send_chat("🌙 Starlight Snuggles is now awake... come relax ✨")

    async def on_user_join(self, user: User):
        await self.send_chat(f"💫 Welcome {user.username} to Starlight Snuggles 🌙")

    async def on_chat(self, user: User, message: str):
        msg = message.lower()

        # 🌙 Greeting
        if msg == "!hi":
            await self.send_chat(f"🌙 hii {user.username} ✨")

        # 💤 Cozy vibe
        elif msg == "!sleep":
            await self.send_chat("💤 drifting into soft starlight dreams...")

        # 🎶 Music command (link-based)
        elif msg.startswith("!play"):
            song = message[6:]
            if song:
                await self.send_chat(f"🎧 now playing: {song} ✨")
            else:
                await self.send_chat("🎶 tell me what to play...")

        # ✨ Random cozy messages
        elif msg == "!vibe":
            vibes = [
                "🌌 the stars are extra soft tonight...",
                "✨ you're safe here, just relax...",
                "🌙 everything feels quieter under starlight...",
                "💫 cozy energy detected..."
            ]
            await self.send_chat(random.choice(vibes))

        # 💖 Ping
        elif msg == "!ping":
            await self.send_chat("✨ i'm here~")
