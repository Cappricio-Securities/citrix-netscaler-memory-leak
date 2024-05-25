#!/usr/bin/env python

"""
 * critix-netscaler-memory-leak
 * critix-netscaler-memory-leak Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
               __                  __                                                                __           __
   ____  ___  / /_______________ _/ /__  _____      ____ ___  ___  ____ ___  ____  _______  __      / /__  ____ _/ /__
  / __ \/ _ \/ __/ ___/ ___/ __ `/ / _ \/ ___/_____/ __ `__ \/ _ \/ __ `__ \/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/
 / / / /  __/ /_(__  ) /__/ /_/ / /  __/ /  /_____/ / / / / /  __/ / / / / / /_/ / /  / /_/ /_____/ /  __/ /_/ / ,<
/_/ /_/\___/\__/____/\___/\__,_/_/\___/_/        /_/ /_/ /_/\___/_/ /_/ /_/\____/_/   \__, /     /_/\___/\__,_/_/|_|
                                                                                     /____/
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mcritix-netscaler-memory-leak : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mcritix-netscaler-memory-leak\033[0m [option]

Usage: \033[92mcritix-netscaler-memory-leak\033[0m [options]

Options:
  -u, --url     URL to scan                                critix-netscaler-memory-leak -u https://target.com
  -i, --input   <filename> Read input from txt             critix-netscaler-memory-leak -i target.txt
  -o, --output  <filename> Write output in txt file        critix-netscaler-memory-leak -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             critix-netscaler-memory-leak --chatid yourid
  -b, --blog    To Read about critix-netscaler-memory-leak Bug            critix-netscaler-memory-leak -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
               __                  __                                                                __           __
   ____  ___  / /_______________ _/ /__  _____      ____ ___  ___  ____ ___  ____  _______  __      / /__  ____ _/ /__
  / __ \/ _ \/ __/ ___/ ___/ __ `/ / _ \/ ___/_____/ __ `__ \/ _ \/ __ `__ \/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/
 / / / /  __/ /_(__  ) /__/ /_/ / /  __/ /  /_____/ / / / / /  __/ / / / / / /_/ / /  / /_/ /_____/ /  __/ /_/ / ,<
/_/ /_/\___/\__/____/\___/\__,_/_/\___/_/        /_/ /_/ /_/\___/_/ /_/ /_/\____/_/   \__, /     /_/\___/\__,_/_/|_|
                                                                                     /____/
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mcritix-netscaler-memory-leak : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
