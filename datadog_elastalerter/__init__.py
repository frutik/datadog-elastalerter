from elastalert.alerts import Alerter, basic_match_string
from datadog import api, initialize


class DatadogAlerter(Alerter):
    required_options = set(['datadog_api_key'])
    required_options = set(['datadog_app_key'])

     def __init__(self, *args):
        super(DatadogAlerter, self).__init__(*args)

        self.api_key = self.rule.get('datadog_api_key')
        self.app_key = self.rule.get('datadog_app_key')

        options = {
            'api_key': self.api_key,
            'app_key': self.app_key
        }
        initialize(**options)

    def alert(self, matches):
        for match in matches:
            text = basic_match_string(self.rule, match)
            title = "Something big happened!"
            tags = ['version:1', 'application:web']

            api.Event.create(title=title, text=text, tags=tags)

    def get_info(self):
        return {'type': 'Datadog Alerter'}
