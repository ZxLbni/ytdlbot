#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - constant.py
# 8/16/21 16:59
#

__author__ = "Noob <dolabani46@gmail.com>"

import os

from config import (
    FREE_DOWNLOAD,
    REQUIRED_MEMBERSHIP,
    TOKEN_PRICE,
)


class BotText:
    start = """
    Welcome to YouTube Download bot. Type /help for more information.

    Join https://t.me/NOOBPrivate for updates."""

    help = """
1. For YouTube and any websites supported by yt-dlp, just send the link and we will download and send it to you.

2. For specific links use `/spdl {URL}`. 

3. If the bot doesn't work, try again or join https://t.me/NOOBPrivate for updates.

4. Wanna deploy it yourself?\nHere's the source code: https://t.me/NOOBPrivate
    """

    about = "YouTube Downloader by @l_abani .\n\nOpen source: https://t.me/NOOBPrivate"

    buy = f"""
**Terms:**
1. You can use this bot to download video for {FREE_DOWNLOAD} times within a 24-hour period.

2. You can buy additional download tokens, valid permanently.

3. Refunds are possible, contact me if you need that @BennyThink

4. Paid user can download files larger than 2GB.

**Price:**
valid permanently
1. 1 USD == {TOKEN_PRICE} tokens
2. 7 CNY == {TOKEN_PRICE} tokens
3. 10 TRX == {TOKEN_PRICE} tokens

**Payment options:**
Pay any amount you want. For example you can send 20 TRX for {TOKEN_PRICE * 2} tokens.
1. Telegram Bot Payment(Stripe), please click Bot Payment button.
4. TRON(TRX), please click TRON(TRX) button.

**After payment:**
1. Telegram Payment & Tron(TRX): automatically activated within 60s. Check /start to see your balance.

Want to buy more token with Telegram payment? Let's say 100? Here you go! `/buy 123`
    """

    private = "This bot is for private use"

    membership_require = f"You need to join this group or channel to use this bot\n\nhttps://t.me/{REQUIRED_MEMBERSHIP}"

    settings = """
Please choose the preferred format and video quality for your video. These settings only **apply to YouTube videos**.

High quality is recommended. Medium quality aims to 720P, while low quality is 480P.

If you choose to send the video as a document, it will not be possible to stream it.

Your current settings:
Video quality: **{0}**
Sending format: **{1}**
"""
    custom_text = os.getenv("CUSTOM_TEXT", "")

    premium_warning = """
    Your file is too big, do you want me to try to send it as premium user? 
    This is an experimental feature so you can only use it once per day.
    Also, the premium user will know who you are and what you are downloading. 
    You may be banned if you abuse this feature.
    """

    @staticmethod
    def get_receive_link_text() -> str:
        return "Your task was added to active queue.\nProcessing...\n\n"
