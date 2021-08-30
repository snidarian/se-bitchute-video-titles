# se-bitchute-video-titles
scrapes today's content by creators in .creators.csv and prints titles and URLs to Stdout


## Program procedure

1. Checks .bitchute_creators.csv file in the CWD for list of Bitchute creators
2. Goes to Bitchute using Selenium firefox webdriver and scrapes data on their recent content (today by default)
3. Returns video titles with URLs by creator to the Stdout of terminal emulator



