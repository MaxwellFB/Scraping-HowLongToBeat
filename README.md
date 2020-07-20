# Scraping-HowLongToBeat

This is a program to scraping the site "howlongtobeat.com". It is only necessary to inform the name of the game that you wish collect information and the program will result data available in the site.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Libraries:
* BeautifulSoup v4.9.1
* Requests v2.22.0

### Installing


To install you can download manually from GitHub or run the following command:

```
git clone https://github.com/MaxwellFB/Scraping-HowLongToBeat.git
```

## Running

First we need to import the main class called HowLongToBeat

```
from howlongtobeat import HowLongToBeat
```

And initialize

```
hltb = HowLongToBeat()
```

### Searching a game

To search a game is necessary to use the complete name of the game. The following example we are searching about "Dark Souls III". Don't worry about sensitive case :)

```
result = hltb.search_game('dark souls iii')
```

### Return game found

If the game we are searching be found all data collect will be stored in the class "HowLongToBeatData" that we can access using the follow command:

```
result.[data_name]
```

Let's get the 'developer':
```
result.developer
'From Software'
```

To check all information collected from the game we can use the follow command:

```
result.__dict__
```

Normally the games don't have all information that we collect because don't exist for that game or nobody submitted yet. These information will be classified as:

```
None
```


### Return game not found

The program looks for the game with the same name that we typed, if you look in the site "howlongtobeat.com" when we search a game using the full name the results list will show an option with a green name.

![HowLongToBeat Green Name](https://user-images.githubusercontent.com/20483869/87887747-3f5a9a80-c9fe-11ea-87d0-3b8cb353b3c4.png)

If the name typed don't result an option with a green name the return will be:

```
False
```

### Story the time

To store the time, was created a class. There we can collect what we want.

If we type only the name we receive a complete time text:
```
result.main_story_time
32 hours 30 minutes 0 seconds
```
To collect only the hour, minutes or seconds:
```
result.main_story_time.hours
32
```
```
result.main_story_time.minutes
30
```
```
result.main_story_time.seconds
0
```
## Contributing

If you have suggestions, found bug, or something wrong. Don't be shy, tell me using the [issue](https://github.com/MaxwellFB/Scraping-HowLongToBeat/issues) or submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Maxwell F. Barbosa** - [MaxwellFB](https://github.com/MaxwellFB)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you [PurpleBooth](https://gist.github.com/PurpleBooth) for providing [README-Template.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
