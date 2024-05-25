#!/usr/bin/env python

"""
 * critix-netscaler-memory-leak
 * critix-netscaler-memory-leak Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
"""
import requests
from utils import const
from utils import configure


def sendmessage(vul):

    data = {"Tname": "critix-netscaler-memory-leak", "chatid": configure.get_chatid(), "data": vul,
            "Blog": const.Data.blog, "bugname": const.Data.bugname, "Priority": "Medium"}

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.put(const.Data.api, json=data, headers=headers)
    except:
        print("Bot Error")
