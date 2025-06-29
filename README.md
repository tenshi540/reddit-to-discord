# Reddit → Discord Bot

A simple Python script that monitors a subreddit for new posts with a specific flair and forwards them to a designated Discord channel.

## Features
- Monitors new posts from a specified subreddit
- Filters posts by flair (e.g. `"Datamined"`)
- Sends matching posts to a Discord channel using a bot
- Runs continuously with customizable check interval

## Technologies
- Python
- [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper)
- [discord.py](https://discordpy.readthedocs.io/)

## Setup

1. Install dependencies:
   ```bash
   pip install praw discord.py
