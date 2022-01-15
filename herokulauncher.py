import os
import time
from bot import MusicBot

# Start Lavalink server
# Run       java -jar Lavalink.jar
# From      [base]\jdk-13.0.2\bin

# os.system("java -jar Lavalink.jar")

# time.sleep(30)


def main():
    bot = MusicBot()
    bot.run()


if __name__ == "__main__":
    main()
