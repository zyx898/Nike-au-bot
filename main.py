# -*- coding: utf-8 -*-
import time
import random
import discord
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
import threading
from discord_webhook import DiscordEmbed, DiscordWebhook

def cart_nike_au(producturl,size):
    driver = webdriver.Chrome()
    driver.get(producturl)
    sizes = driver.find_elements_by_class_name('css-xf3ahq')
    for sizeinhtml in (sizes):
        if size in (sizeinhtml.text.split('/')[0]):
            break

    sizeinhtml.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="buyTools"]/div[2]/button[1]').click()
    time.sleep(3)
    driver.get('https://www.nike.com/au/en/cart')
    while 'cart' not in driver.current_url:
        time.sleep(2)
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div[6]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div[4]/div/div/button[1]').click()
    except:
        driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/aside/div[5]/div/button[1]').click()

    time.sleep(2)
    while "checkout" not in driver.current_url:
        time.sleep(2)
    return (driver.current_url)



client = discord.Client()

@client.event
async def on_ready():
    print("NIKE AU BOT")
    print('Logged in as %s' %client.user.name)
    print("Client User ID: %s" %client.user.name)
    print('------')
    game = discord.Game("NIKE AU CART")
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith('!nikecartAU'):
        producturl = 'https://www.nike.com/au/t/xyisthebossman/'+message.content.split(" ")[1]
        cartsize = message.content.split(" ")[2]
        carturl = cart_nike_au(producturl,cartsize)
        embed = discord.Embed(title='Nike AU Cart',description='Wrote by XY in 20 minutes',color=0x36393F)
        embed.add_field(name='Cart Link', value=carturl,inline=True)
        embed.set_author(name='@zyx898')
        embed.set_footer(text='@zyx898 | SkrNotify',icon_url='https://pbs.twimg.com/profile_images/1134245182738718721/N12NVkrt_400x400.jpg')
        await message.channel.send(embed=embed)


client.run('')## put your bot token
