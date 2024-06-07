from typing import NamedTuple


class EnvDict(NamedTuple):
    LOG_LEVEL_ROOT: int
    LOG_LEVEL_CK: int
    DISCORD_CLIENT_TOKEN: str
    SHOULD_SYNC_COMMANDS: str
    INACTIVITY_TIMEOUT_SECONDS: int
    SPOTIPY_CLIENT_ID: str
    SPOTIPY_CLIENT_SECRET: str
    SPOTIPY_REDIRECT_URI: str
    SPOTIPY_SCOPE: str
    SPOTIFY_USERNAME: str
    YOUTUBE_DATA_API_V3_KEY: str
    # FF_VOICE: int
