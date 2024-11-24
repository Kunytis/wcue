# ЭТО ПРОСТО ТЕСТ ЭТО НЕ ПРОГРАММА ЭТО ПРОСТО ТЕСТ ЭТО НЕ ПРОГРАММА ЕКЗАМЕН В revive.py!!!!
































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

    class SiteParser:
        def __init__(self, url):
            self.url = url
            self.content = self.site_content()

    def site_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text().lower()
        except requests.exceptions.RequestException:
            print("Error, (Iryna was here)")  # This can be a custom error message
            return ''

    def search(self, query):
        if not self.content:
            return 0
        return len(re.findall(query.lower(), self.content))

    class UserInterface:
        def __init__(self, app):
            self.app = app

        def add_site(self):
            url = input("Enter site URL: ")
            self.app.site_manager.add_site(url)

        def display_sites(self):
            sites = self.app.site_manager.get_sites()
            if sites:
                print("Sites List:")
                for site in sites:
                    print(site)
            else:
                print("No sites available.")

        def search_sites(self):
            query = input("Enter search query: ")
            results = self.app.search_sites(query)
            if results:
                print("Search Results:")
                for site, matches in results:
                    print(f"{site}: {matches} matches")
            else:
                print("No results found.")

    class SearchApp:
        def __init__(self):
            self.site_manager = ManagerFCIT()
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

app = ManagerFCIT.SearchApp()
app.run()