import requests
import sys
from bs4 import BeautifulSoup
# Hacker News article find system
response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find(id="hnmain")
# to find all <a> tags withing the body
atags = table.select(".titleline > a")
# to find all scores of points in format nn points
score = table.select(".subline .score")

# take one argument of point are needed by user to get article with highest or or same point range
def point_value(point):
    for i, value in enumerate(atags):
        score_points = int(score[i].text.split(" ")[0])
        if score_points >= point:
            print(f"Blog: {value.text}, and it's points: {score[i].text}")

# taking one system argument, convert it into number and then apply it to the function
points = sys.argv[1:2]
point_value(int(points[0]))
# end of application