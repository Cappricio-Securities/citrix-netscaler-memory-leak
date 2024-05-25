#!/usr/bin/env python

"""
 * critix-netscaler-memory-leak
 * critix-netscaler-memory-leak Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""


def writedata(output, data):
    with open(output, 'a') as file:
        file.write(data)
