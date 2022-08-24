from src.command.command import bot
from src.creds import get_secret_key

def main():
    bot.run(get_secret_key())


if __name__ == '__main__':
    main()
