# ЭТО ЕКЗАМЕН НО Я ИСПОЛЬЗОВАЛА ДРУГОЙ ПРОЕКТ ДЩЛЯ ТЕСТА ЧТО БЫ НИЧЕГО НЕ МЕШАЛО!!!!!!










class ManagerFCIT:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
        else:
            print(f"error, {url} already exists!")

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
            self.ui = ManagerFCIT.UserInterface(self)

        def search_sites(self, query):
            results = []
            for site in self.site_manager.get_sites():
                parser = ManagerFCIT.SiteParser(site)
                matches = parser.search(query)
                if matches > 0:
                    results.append((site, matches))
            return sorted(results, key=lambda x: x[1], reverse=True)

        def run(self):
            while True:
                print("1. Add site")
                print("2. Show all sites")
                print("3. Search")
                print("4. Exit")

                choice = input("Choose an option: ")

                if choice == '1':
                    self.ui.add_site()
                elif choice == '2':
                    self.ui.display_sites()
                elif choice == '3':
                    self.ui.search_sites()
                elif choice == '4':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice, please try again.")


app = ManagerFCIT.SearchApp()
app.run()