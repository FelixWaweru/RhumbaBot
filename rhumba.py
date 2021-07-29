from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
from random import *

links = [
    "https://www.youtube.com/watch?v=-m0t82t12SY",
    "https://www.youtube.com/watch?v=B8wTeA88j2c",
    "https://www.youtube.com/watch?v=iRDojQzp5B4",
    "https://www.youtube.com/watch?v=4ZJcnIWQUp4",
    "https://www.youtube.com/watch?v=QFG9lp1Wh_U",
    "https://www.youtube.com/watch?v=QFG9lp1Wh_U",
    "https://www.youtube.com/watch?v=OG4_YXfqn60",
    "https://www.youtube.com/watch?v=SDD7BOCM5dc",
    "https://www.youtube.com/watch?v=2bns3aHaTBo",
    "https://www.youtube.com/watch?v=W-FLN9VQdBc",
    "https://www.youtube.com/watch?v=Fr175wk_Ei0",
    "https://www.youtube.com/watch?v=DEWyViZRgrw",
    "https://www.youtube.com/watch?v=H8tTSsc7bwU",
    "https://www.youtube.com/watch?v=ueN1k6uOAaA",
    "https://www.youtube.com/watch?v=hsNELIbS8CA",
    "https://www.youtube.com/watch?v=lpre4VIyUM8",
    "https://www.youtube.com/watch?v=gSA6xt4AXRg",
    "https://www.youtube.com/watch?v=i5grymygAaI",
    "https://www.youtube.com/watch?v=gIJNr1sELQw",
    "https://www.youtube.com/watch?v=T33rO0ZgUUo",
    "https://www.youtube.com/watch?v=Sj-1oHlXGU0",
    "https://www.youtube.com/watch?v=Sj-1oHlXGU0",
    "https://www.youtube.com/watch?v=Gqvi0zdN-tM",
    "https://www.youtube.com/watch?v=_JTWuPjW6Dw",
]





    




for i in range(10):
    print("Loop " + str(i))
    # The Minutes interval
    wait = randint(5, 15)

    # The random Video selector
    vid = randint(0, len(links)-1)
    
    # Open browser using Selenium
    driver = webdriver.Firefox()
    driver.get(links[vid])

    print("Playing: " + links[vid])

    # Accept Cookies
    try:
        driver.find_element_by_xpath('/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button').click()
        print("Cookies Accepted")
    except:
        pass

    # Play Video
    time.sleep(8)
    print("Playing Vid")
    # wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()

    #Skip Ad
    try:
        skipAd = driver.find_element_by_xpath("xpath for next /html/body/div[2]/div[4]/div/div[4]/div[2]/div[2]/div/div[4]/div/div/div[5]/button").click()
    except:
        pass

    # Chill while video loads and plays
    time.sleep(20)
    print("Done")

    driver.close()
    
    time.sleep(wait)