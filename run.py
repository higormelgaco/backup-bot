import logging
from myBackup import report_bot
logger = logging.getLogger('Backup-Bot')
logger.setLevel(logging.DEBUG)
print(f'{"="*34}\n[*] - Backup-Bot v1.0\n[*] - By: higormelgaco@yandex.com\n{"="*34}')

def main():
    bot = report_bot.my_bot()
    try:
        bot.megaBot()
    except KeyboardInterrupt:
        logger.info('\n[*] - Programa interrompido')

if __name__ == '__main__':
    main()