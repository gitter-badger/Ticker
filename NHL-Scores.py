# Author: John Freed
# Python Version 2.7

# You must enter the team name exactly as it appears
# on http://www.nhl.com/ice/scores.htm

import os
import platform
import sys
import time
import urllib2
from bs4 import BeautifulSoup

refresh_time = 60  # Refresh time (Seconds)
score_url = 'http://www.nhl.com/ice/scores.htm'
games = [['New Jersey', 'Tampa Bay'], ['NY Rangers', 'Ottawa'], ['Minnesota', 'Nashville']]

def main():

    clear_screen()
    print_ascii_art()
    time.sleep(3)

    while True:
        clear_screen()

        # Try to make sure the user set everything up correctly
        for match in games:
            if len(match) > 2:
                print 'It looks like you have more than 2 teams playing each other in a single game!'
                print 'Check your "games" variable and try again.'
                sys.exit()

        # Check the scores!
        for match in games:
            print_header()

            for team in match:
                team_score = get_score(team)

                if team_score != -1:
                    print team + ': ' + team_score
                else:
                    print 'Error occurred. Team: ' + team

            print ''

        print ''

        # Perform the sleep
        for x in range(0, refresh_time):
            sys.stdout.write("Waiting... " + str(x) + "/" + str(refresh_time) + "\r")
            time.sleep(1)


def get_score(team):
    # Get the page and read it in to BeautifulSoup
    page = urllib2.urlopen(score_url)
    page_html = page.read()
    soup = BeautifulSoup(page_html)

    team_list = soup.find('a', text = team)

    try:
        for td in team_list.parent.find_next_siblings('td', class_ = 'total'):
            current_score = td.text
            return current_score
    except:
        return -1


def print_header():
    print '======================'
    print '= Current NHL Scores ='
    print '======================'


def print_ascii_art():
    # Thanks Cheshirecat from http://www.retrojunkie.com/asciiart/sports/hockey.htm !
    print "                        .---."
    print "                       /_____\\"
    print "                      _HH.H.HH"
    print "       _          _-\"\" WHHHHHW\"\"--__"
    print "       \\\\      _-\"   __\\VW=WV/__   /\"\"."
    print "        \\\\  _-\" \\__--\"  \"-_-\"   \"\"\"    \"_"
    print "         \\\\/ PhH  _                      \"\""
    print "          \\\\----_/_|     ___      /\"\\  T\"\"\\====-"
    print "           \\\\ /\"-._     |%|H|    (   \"\\|) | /  .:)"
    print "            \\/     /    |-+-|     \\    |_ J .:::-'"
    print "            /     /     |H|%|  _-' '-._  \" )/;\""
    print "           /     / \\    __    (  \\ \\   \\   \""
    print "          /     /\\/ '. /  \\   \\ \\ \\ _- \\"
    print "          \"'-._/  \\/  \\    \"-_ \\ -\"\" _- \\"
    print "         _,'\\\\  \\  \\/  )      \"-, -\"\"    \\"
    print "      _,'_- _ \\\\ \\  \\,'          \\ \\_\\_\\  \\"
    print "    ,'    _-    \\_\\  \\            \\ \\_\\_\\  \\"
    print "    \\_ _-   _- _,' \\  \\            \\ \"\"\"\"   )"
    print "     C\\_ _- _,'     \\  \"--------.   L_\"\"\"\"_/"
    print "      \" \\/-'         \"-_________|     '\"-Y"
    print ""
    print "             NHL Scores by John Freed"


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    main()