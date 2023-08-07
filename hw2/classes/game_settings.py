
class Game_settings:
    '''
    Sets game settings
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __del__(self):
        Game_settings._instance = None

    def __init__(self, sound_enabled, difficulty_level):
        self.sound_enabled = sound_enabled
        self.difficulty_level = difficulty_level

    def update_settings(self, sound_enabled, difficulty_level):
        self.sound_enabled = sound_enabled
        self.difficulty_level = difficulty_level