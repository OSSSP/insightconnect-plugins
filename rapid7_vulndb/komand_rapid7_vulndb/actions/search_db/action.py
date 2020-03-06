import komand
from .schema import SearchDbInput, SearchDbOutput, Input, Output
# Custom imports below
from komand_rapid7_vulndb.util import path_helper, browser


class SearchDb(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_db',
                description='Search the database to find vulnerabilities and exploits',
                input=SearchDbInput(),
                output=SearchDbOutput())

    def run(self, params={}):
        # Get params
        search = params.get(Input.SEARCH)
        data_base = params.get(Input.DATABASE)

        search = search.replace(" ", "+")
        self.logger.info(f'Searching for {search}')

        # Set database xpath
        temp = path_helper.set_xpath(data_base)
        xpath = temp['xpath']
        db = temp['db']
        self.logger.info('Database set')

        # Create web browser
        base_url = f'https://www.rapid7.com/db/search?utf8=%E2%9C%93&q={search}&t={db}'
        vuldb_browser = browser.VulnDBBrowser(data_base)
        results = vuldb_browser.scrape_vuldb(base_url, xpath)
        print(f"RESULTS: {results}")
        if results['results']:
            return {Output.SEARCH_RESULTS: results['results'], Output.RESULTS_FOUND: results['found']}
        else:
            return {Output.RESULTS_FOUND: results['found']}
