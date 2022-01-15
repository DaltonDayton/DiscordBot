from bot import MusicBot

# Start Lavalink server
# Run       java -jar Lavalink.jar
# From      [base]\jdk-13.0.2\bin

os.system(".\\jdk-13.0.2\\bin\\java -jar .\\jdk-13.0.2\\bin\\Lavalink.jar")


def main():
    bot = MusicBot()
    bot.run()


if __name__ == "__main__":
    main()
