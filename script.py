import praw
import discord
import asyncio

# === Configuration ===
DISCORD_TOKEN = "X"
CHANNEL_ID = 1  # Replace with your Discord channel ID

REDDIT_CLIENT_ID = "X"
REDDIT_CLIENT_SECRET = "X"
REDDIT_USER_AGENT = "hsrscraper by u/tenshi540"

SUBREDDIT = "HonkaiStarRail_leaks"
FLAIR_KEYWORD = "Datamined"
FETCH_LIMIT = 50
CHECK_INTERVAL = 60  # seconds

# === Reddit Setup ===
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# === Discord Setup ===
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# === Memory storage for last-handled post ===
last_handled_post_time = 1747717352

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await monitor_reddit()


async def monitor_reddit():
    global last_handled_post_time
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while True:
        try:
            subreddit = reddit.subreddit(SUBREDDIT)
            new_posts = subreddit.new(limit=FETCH_LIMIT)

            for post in reversed(list(new_posts)):  # Reverse to post older ones first
                if (
                    post.link_flair_text
                    and FLAIR_KEYWORD in post.link_flair_text
                    and post.created_utc > last_handled_post_time
                ):
                    message = f"**[DATAMINED]** {post.title}\n{post.url}"
                    await channel.send(message)
                    last_handled_post_time = post.created_utc

        except Exception as e:
            print(f"Error while checking Reddit: {e}")

        await asyncio.sleep(CHECK_INTERVAL)


client.run(DISCORD_TOKEN)
