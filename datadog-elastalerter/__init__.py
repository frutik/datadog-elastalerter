from elastalert.alerts import Alerter, basic_match_string

class DatadogAlerter(Alerter):
    required_options = set(['datadog_api_key'])

    def alert(self, matches):
        for match in matches:

            # Config options can be accessed with self.rule
            with open(self.rule['output_file_path'], "a") as output_file:

                # basic_match_string will transform the match into the default
                # human readable string format
                match_string = basic_match_string(self.rule, match)

                output_file.write(match_string)

    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'Datadog Alerter',
                'output_file': self.rule['output_file_path']}
