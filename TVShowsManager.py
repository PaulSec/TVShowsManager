from eztv_api import EztvAPI
from ConfigParser import SafeConfigParser
import os
import time
import sys

CONFIG_FILE = "./config.ini"

parser = SafeConfigParser()
parser.read(CONFIG_FILE)

USER = parser.get("config", "username")
PASS = parser.get("config", "password")
IP = parser.get("config", "ip")
TIMER = int(parser.get("config", "timer"))
VERBOSE_MODE = False

parser = SafeConfigParser()


def display_message(message):
    global VERBOSE_MODE

    if (VERBOSE_MODE):
        print message


def download(magnet):
    global IP, USER, PASS

    cmd = "transmission-remote "
    cmd = cmd + "%s -n %s:%s --add '%s'" % (IP, USER, PASS, magnet)
    print cmd
    os.system(cmd)


def update_tv_show(name, season, episode):
    global parser

    parser.set(name, 'season', season)
    parser.set(name, 'episode', episode)


def iterate_on_seasons(seasons, name):
    global parser

    old_season = int(parser.get(serie, "season"))
    old_episode = int(parser.get(serie, "episode"))

    display_message("Found %s seasons" % (len(seasons) + 1))
    for season in seasons:
        for episode in seasons[season]:
            if (season > old_season or (season == old_season and episode > old_episode)):
                display_message("Updating ! Season %s, Episode %s" % (str(season), str(episode)))
                download(seasons[season][episode])
                old_season = season
                old_episode = episode

    update_tv_show(name, str(old_season), str(old_episode))


def update_config_file():
    global parser, CONFIG_FILE

    with open(CONFIG_FILE, 'wb') as configfile:
        parser.write(configfile)

if (sys.argv[1] == "--v"):
    VERBOSE_MODE = True

while True:
    parser.read(CONFIG_FILE)
    for serie in parser.sections():
        # iterate on all series
        if (serie != "config"):
            try:
                display_message("Checking for TV Show %s" % (serie))
                test_api = EztvAPI().tv_show(serie)
                iterate_on_seasons(test_api.seasons(), serie)
                update_config_file()
            except Exception, err:
                print Exception, err
        else:
            pass
    time.sleep(float(TIMER * 10))
