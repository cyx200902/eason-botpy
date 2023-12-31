from .api import BotAPI
from .types import interaction, gateway


class Interaction:
    __slots__ = ("_api", "_ctx", "id", "application_id", "type", "event_id", "data", "guild_id", "channel_id")

    def __init__(self, api: BotAPI, event_id, data: interaction.InteractionPayload):
        self._api = api

        self.id = data.get("id", None)
        self.type = data.get("type", None)
        self.application_id = data.get("application_id", None)
        self.event_id = event_id
        self.data = data.get("data", None)
        self.guild_id = data.get("guild_id", None)
        self.channel_id = data.get("channel_id", None)

    def __repr__(self):
        return str({items: str(getattr(self, items)) for items in self.__slots__ if not items.startswith('_')})
