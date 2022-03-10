import pyto as ui
from ScraperClass import PostScraper
"""A UI that lets you scrape reddit popular post category 
and article contents of that specific post"""

"""Status: uncompleted, work in progress."""
view = ui.View()

view.background_color = ui.Color.white(1,1)

class buttons:
    def __init__(self):
        self.button = ui.Button(title="Scrape")
        self.button.background_color = ui.COLOR_BLACK
        self.button.size = (100, 50)
        self.button.center = (view.width/2, view.height/2)
        view.add_subview(self.button)

    def generate(self):
        return self.button

buttonObj = buttons()
button = buttonObj.generate()

textBox = ui.TextField(placeholder="Type here")
textBox.size = (200, 50)
textBox.center = (view.width/2, view.height/3)
view.add_subview(textBox)

ui.show_view(view, ui.PRESENTATION_MODE_FULLSCREEN)

class ScrapeUI:
    def collect_info(text):
        url = PostScraper(text)
        url.view_popular_posts()

    button.action = collect_info(textBox.text)

scrapeObj = ScrapeUI()

