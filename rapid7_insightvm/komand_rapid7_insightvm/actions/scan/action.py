import komand
from .schema import ScanInput, ScanOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class Scan(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan',
                description='Start a scan on a site',
                input=ScanInput(),
                output=ScanOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        site_id = params.get("site_id")
        endpoint = endpoints.Scan.site_scans(self.connection.console_url,
                                             site_id)
        self.logger.info("Using %s ..." % endpoint)
        response = resource_helper.resource_request(endpoint=endpoint, method='post')

        return response
