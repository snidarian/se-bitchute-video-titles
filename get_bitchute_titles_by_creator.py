#!/usr/bin/python3
# Program will take one argument (Bitchute creator name) an unlimited amount of times
# will return all titles from current date and print them to screen by creator
# this program has one limitation - It can only retrieve the 25 most recent videos by each creator


# Setup selenium and Firefox browser
from selenium import webdriver
from selenium.webdriver.firefox import service
# Service class and option class fixes
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# import the keys class
from selenium.webdriver.common.keys import Keys

# needed to help direct the programs scraping
import argparse
# greater control of terminal from script
import os
# terminal coloring
from colorama import Fore

# dev dependency
import time
# creators_list.csv will be used to store the current creators wanted
import csv

OPTIONS = Options()
OPTIONS.add_argument("--headless")

# will eventually run headlessly
OPTIONS.headless = True

#driver = webdriver.Firefox(options=OPTIONS)
driver = webdriver.Firefox(options=OPTIONS)


# needed to help direct the programs scraping
import argparse
# greater control of terminal from script
import os
# terminal coloring
from colorama import Fore

# dev dependency
import time
# creators_list.csv will be used to store the current creators wanted
import csv


# setup colored ansi terminal escape sequences
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
reset = Fore.RESET


def main() -> None:
    creators_list = []
    # Read creators_list.csv to gather channelurls
    # These should look like this
    # https://www.bitchute.com/channel/[channel-string-or-name]/
    with open("creators_list.csv", mode='r') as creator_csv:
        creator_reader = csv.reader(creator_csv, delimiter=',')
        for row in creator_reader:
            creators_list.append(row)
    
    for channel_url in creators_list:
        driver.get(channel_url[0])
        channel_title = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[3]/div[1]/div/div/div[3]/p[1]/a').text
        time.sleep(1)
        print(f"{red}\n\n\t\t{channel_title}\n{reset}")
        for video in range(1, (args.count + 1)):
            # print each video title, url, and date
            video_title = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[{video}]/div/div[2]/div/div[2]/a').text
            video_link = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[{video}]/div/div[2]/div/div[2]/a').get_attribute('href')
            video_date = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[{video}]/div/div[2]/div/div[1]/span').text            
            print(f"{green}{video_date}{reset} - {video_title}")
            print(f"\t{yellow}{video_link}{reset}\n")


if __name__ == "__main__":
    # setup argparse
    parser = argparse.ArgumentParser(description="Automates getting info about Bitchute channels recent videos")
    args = parser.add_argument("-c", "--count", help="[count] of most recent videos", type=int, default=10)
    args = parser.parse_args()
    main()







