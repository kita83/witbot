from slackbot.bot import Bot


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    from dotenv import load_dotenv
    load_dotenv()
    main()

