from bs4 import BeautifulSoup
import requests
#div class='Description'
class PostScraper:
    def __init__(self, link):
        self.link = link
        self.req_link = requests.get(self.link)
        self.soup = BeautifulSoup(self.req_link.content, "html.parser")

        self.h3_tags_title = [str(header.text) for header in self.soup.find_all('h3', {'class': '_eYtD2XCVieq6emjKBH3m'})]
        self.links_to_post = [link.get('href') for link in self.soup.find_all('a') if 'https://www.reddit.com/r/' in link.get('href')]
        self.time_posted = [str(t.text) for t in self.soup.find_all(target="_blank") if t.text[0].isdigit()]
        self.border = "-"*60
        self.title = "\t\tPopular Posts"

    def view_popular_posts(self):
        dictt = {}
        string = "\nTime Posted:"
        index_tp = 0 #time posted index
        print(self.title.upper())
        print(self.border)

        for i, t in enumerate(self.h3_tags_title, start=1):
            dictt[i] = t + string + str(self.time_posted[index_tp]) + "\n"
            index_tp += 1
        for k, v in dictt.items():
            print(str(k) + ".", v)
            print(self.border)

class _Article(PostScraper):
    def __init__(self, link):
        self.link = link
        self.req_link = requests.get(self.link)
        self.soup = BeautifulSoup(self.req_link.content, "html.parser")

        videotag = self.soup.body.find_all("div", id="t3_t90egr")
        print(videotag)
#ScraperObj = PostScraper("https://www.reddit.com")

#articleObj = _Article("https://www.reddit.com/r/Unexpected/comments/t90egr/christopher_lee_is_scarier_than_saruman/")