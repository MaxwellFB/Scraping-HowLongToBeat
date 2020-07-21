"""Stucture to store all data collect from the game."""


class HowLongToBeatData():
    """Stucture to store all data from the game."""

    def __init__(self):
        """Structure of the data."""
        # Game datas
        self.game_name = None
        self.url_game = None
        self.game_id = None
        self.synopsis = None
        self.type = None
        self.developer = None
        self.publisher = None
        self.playable_on = None
        self.genre = None

        # Top bar with time
        self.main_story_time = None
        self.main_extras_time = None
        self.completionist_time = None
        self.all_styles_time = None
        self.single_player_time = None
        self.coop_time = None
        self.vs_time = None

        # Time table single-player
        self.sp_main_story_polled = None
        self.sp_main_story_average = None
        self.sp_main_story_median = None
        self.sp_main_story_rushed = None
        self.sp_main_story_leisure = None
        self.sp_main_extras_polled = None
        self.sp_main_extras_average = None
        self.sp_main_extras_median = None
        self.sp_main_extras_rushed = None
        self.sp_main_extras_leisure = None
        self.sp_completionists_polled = None
        self.sp_completionists_average = None
        self.sp_completionists_median = None
        self.sp_completionists_rushed = None
        self.sp_completionists_leisure = None
        self.sp_all_playstiles_polled = None
        self.sp_all_playstiles_average = None
        self.sp_all_playstiles_median = None
        self.sp_all_playstiles_rushed = None
        self.sp_all_playstiles_leisure = None
