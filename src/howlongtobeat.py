"""
Main class

This is a program to scraping the site "howlongtobeat.com".
"""

from bs4 import BeautifulSoup as bs
import requests
from hltb_data import HowLongToBeatData
from hltb_time import Time
bs

class HowLongToBeat():
    """Search and collect data from game in the site HowLongToBeat."""

    def __init__(self):
        """Store the sites that will be used."""
        self.__url_main = 'https://howlongtobeat.com/'
        self.__url_searcher = 'https://howlongtobeat.com/search_results.php'

    def search_game(self, game_name,
                    about_game=True, top_bar=True, table_sp=True):
        """Search and collect the url of the game in HowLongToBeat."""
        self.about_game = about_game
        self.top_bar = top_bar
        self.table_sp = table_sp
        # Clean data
        self.data = HowLongToBeatData()

        form_data = {
            'queryString': game_name,
            't': 'games',
            'sorthead': 'popular',
            'sortd': 'Normal Order',
            'plat': '',
            'length_type': 'main',
            'length_min': '',
            'length_max': '',
            'detail': '0'
        }

        html = requests.post(self.__url_searcher, data=form_data)
        html_search_list = bs(html.text, 'html.parser')

        # Take what has the identical name (green name)
        game_line = html_search_list.find('a', {'class': 'text_green'})
        # Game not found
        if game_line is None:
            return False

        # Create game url
        href = game_line['href']
        self.data.url_game = self.__url_main + href
        self.data.game_id = int(href[href.find('id')+3:])

        self._find_game_data()
        return(self.data)

    def _find_game_data(self):
        """Collect and store data of the game."""
        html = requests.post(self.data.url_game)
        html_game = bs(html.text, 'html.parser')
        self.data.game_name = html_game.find('div', {'class':
                                             'profile_header shadow_text'}
                                             ).text.strip()

        if self.about_game:
            about_game = html_game.find_all('div', {'class':
                                            'in back_primary shadow_box'}
                                            )[2]
            self._collect_about_game(about_game)

        if self.top_bar:
            top_bar = html_game.find('div', {'class': 'game_times'})
            # Some games don't have upper bar
            if top_bar is not None:
                top_bar_list = top_bar.find_all('li')
                self._collect_top_bar(top_bar_list)

        if self.table_sp:
            table_sp = html_game.find('table', {'class': 'game_main_table'})
            if (table_sp is not None and
                    table_sp.find('td').text == 'Single-Player'):
                self._collect_table_sp(table_sp)

    def _collect_about_game(self, about_game):
        """Collect and store data of the html game profile."""
        synopsis = about_game.find('p')
        if synopsis is not None:
            self.data.synopsis = synopsis.text.strip()

        about_game_profile = about_game.find('div').find_all('div')
        for item in about_game_profile:
            title = item.contents[1].text.strip()
            if 'Type' in title:
                self.data.type = item.contents[2].strip()
            elif 'Developer' in title:
                self.data.developer = item.contents[2].strip()
            elif 'Publisher' in title:
                self.data.publisher = item.contents[2].strip()
            elif title == 'Playable On:':
                self.data.playable_on = item.contents[2].strip()
            elif 'Genre' in title:
                self.data.genre = item.contents[2].strip()

    def _collect_top_bar(self, top_bar_list):
        """Collect and store data of the html upper bar time."""
        for item in top_bar_list:
            time = self._format_time(item.find('div').text, type=1)
            title = item.find('h5').text
            if title == 'Main Story':
                self.data.main_story_time = time
            elif title == 'Main + Extras':
                self.data.main_extras_time = time
            elif title == 'Completionist':
                self.data.completionist_time = time
            elif title == 'All Styles':
                self.data.all_styles_time = time
            elif title == 'Single-Player':
                self.data.single_player_time = time
            elif title == 'Co-Op':
                self.data.coop_time = time
            elif title == 'Vs.':
                self.data.vs_time = time

    def _collect_table_sp(self, table_sp):
        """Collect and store time of the html Single-Player table."""
        table_lines = table_sp.find_all('tbody')
        for line in table_lines:
            line_columns = line.find_all('td')
            time = [self._format_time(line_columns[i].text, type=2)
                    for i in range(2, 6, 1)]
            pooled = line_columns[1].text.strip()

            if line_columns[0].text == 'Main Story':
                self.data.sp_main_story_polled = pooled
                self.data.sp_main_story_average = time[0]
                self.data.sp_main_story_median = time[1]
                self.data.sp_main_story_rushed = time[2]
                self.data.sp_main_story_leisure = time[3]
            elif line_columns[0].text == 'Main + Extras':
                self.data.sp_main_extras_polled = pooled
                self.data.sp_main_extras_average = time[0]
                self.data.sp_main_extras_median = time[1]
                self.data.sp_main_extras_rushed = time[2]
                self.data.sp_main_extras_leisure = time[3]
            elif line_columns[0].text == 'Completionists':
                self.data.sp_completionists_polled = pooled
                self.data.sp_completionists_average = time[0]
                self.data.sp_completionists_median = time[1]
                self.data.sp_completionists_rushed = time[2]
                self.data.sp_completionists_leisure = time[3]
            elif line_columns[0].text == 'All PlayStyles':
                self.data.sp_all_playstiles_polled = pooled
                self.data.sp_all_playstiles_average = time[0]
                self.data.sp_all_playstiles_median = time[1]
                self.data.sp_all_playstiles_rushed = time[2]
                self.data.sp_all_playstiles_leisure = time[3]

    def _format_time(self, line, type=1):
        """Receive a string with time and format to class Time."""
        time = line.split()
        if type == 1:
            # If exist "time unit_of_time"
            # If exist more then 1 time in line, take only the fist
            if len(time) >= 2:
                hours = 0
                mins = 0
                if time[1] == 'Hours':
                    hours = time[0]
                elif time[1] == 'Mins':
                    mins = time[0]
                return Time(hours, mins)
        elif type == 2:
            # timeUnit_of_time
                hours = 0
                mins = 0
                for i in range(len(time)):
                    if time[i][-1] == 'h':
                        hours = time[i][:-1]
                    elif time[i][-1] == 'm':
                        mins = time[i][:-1]
                return Time(hours, mins)
        return None
