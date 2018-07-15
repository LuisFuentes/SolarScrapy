import scrapy

class PlanetsSpider(scrapy.Spider):
    name = 'planets'

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_exoplanets_(full)'
    ]
    # define a custom start_requests
    #def start_requests(self):
    #    urls = ['https://en.wikipedia.org/wiki/List_of_exoplanets_(full)']
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)
    @staticmethod
    def fetch_columns(table_headers):
        '''
            Fetches the column names from the page's table
            and returns them as a list.
        '''
        columns = []
        for col in table_headers:
            # Get the column name from the linkbutton or text
            column_name = ''
            if col.css('a::attr(title)'):
                column_name = col.css('a::attr(title)').extract_first()
            else:
                column_name = col.css('th::text').extract_first().rstrip()
            columns.append(column_name)
        return columns

    @staticmethod
    def fetch_planets(planet_rows):
        '''
            Fetches the planets and returns them as a list of dictionaries.
        '''
        planets_list = []
        for row in planet_rows[1:]:
            planet_name = ''
            planet_dict = {}
            i = 0
            for col in row.css('td'):
                if i == 0:
                    if col.css('a::attr(title)'):
                        planet_name = col.css('a::attr(title)').extract_first()
                        planet_dict[planet_name] = {}
                elif planet_name != '':
                    info = col.css('td::text').extract_first()
                    column = ''
                    if i == 1:
                        column = 'JupiterMass'
                    if i == 2:
                        column = 'JupiterRadius'
                    if i == 3:
                        column = 'OrbitalPeriod'
                    if i == 4:
                        column = 'Axes'
                    if i == 5:
                        column = 'PlanetaryEquilibrium'
                    planet_dict[planet_name][column] = info
                i += 1

            planets_list.append(planet_dict)
        return planets_list

    def parse(self, response):
        # Return the columne names
        '''
            Parses the provided table.
            Fetches the columns and planet information.
        '''
        table_header = response.css('table.wikitable').css('tr')[0].css('th')
        columns = self.fetch_columns(table_header)

        yield {
            'columns': columns
        }

        table_rows = response.css('table.wikitable').css('tbody').css('tr')
        planets_list = self.fetch_planets(table_rows)

        yield {
            'planet': planets_list
        }
