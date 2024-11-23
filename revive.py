import request
from bs4 import BeautifulSoup
import re

class ManagerFCIT:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
        else:
            print("error, {url} already exists! ")

    def get_sites(self):
        return self.sites

    class SitePrser:
        def __init__(self, url):

    def site_content(self):
        try:
            response = request.get(self.url)
            response.raise_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().lower()
    except requests.exceptions.RequestException
        print("error, (Iryna was here)")
        return ""

    def search(self, query):
        if not self.content:
            return 0
        return len(re.findall(query.lower(), self.content))

    class UserInterface:
        def __init__(self, app):
            self.app = app

    class SearchApp:
        def __init__(self):
            self.site_manager = SiteManager()
            self.site_parser = None
            self.ui = UserInterface(self)

    class SearchApp:
        def __init__(self):
            self.site_manager = SiteManager()
            self.site_parser = None
            self.ui = UserInterface(self)


        def search_sites(self, query):
            results = []
            for site in self.site_manager.get_sites():
                parser = SiteParser(site)
                matches = parser.search(query)
                if matches > 0:
                results.append((site, matches))

            return sorted(results, key=lambda x: x[1], reverse=True)

        def run(self):
            while True:
                print("1. add site")
                print("2. show all sites")
                print("3. search")
                print("4. EXIN")

                choise = input("choose smth")

                if choise == '1':
                    self.ui.add_site()
                elif choise == '2':
                    self.ui.display_sites()
                elif choise == '3':
                    self.ui.search_sites()
                elif choise == '4':
                    print("exiting...")
                    break
                else:
                    print("try choosing something!")

if __name__ == "__main__":
    app = SearchApp()
    app.run()