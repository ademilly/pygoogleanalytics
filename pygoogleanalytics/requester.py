# -*- coding: utf-8 -*-
"""requester module provides a Request class providing methods for handling
google analytics API request
"""


class Requester(object):
    """Requester class abstracts google analytics API request writing
    and execution
    """

    def __init__(self, api):
        """Initialize Requester object

        Args:
            `api`   (api_caller.APICaller)  APICaller object
        """

        self.api = api
        self.response = {}

    def build_request(self):
        """Initialize request dictionary representation

        Returns:
            self: for method chaining
        """

        self.request = {
            'samplingLevel': 'LARGE',
            'dateRanges': [],
            'metrics': [],
            'dimensions': [],
            'segments': []
        }

        return self

    def for_view(self, view_id):
        """Set `viewId` property in request dictionary representation

        Args:
            `view_id`   (str)   string representation
                of google-analytics viewID

        Returns:
            self: for method chaining
        """

        self.request['viewId'] = view_id

        return self

    def between(self, start_date, end_date):
        """Set date range in request dictionary representation

        Args:
            `start_date`    (str)   ISO string representation
                of starting period day
            `end_date`      (str)   ISO string representation
                of ending period day

        Returns:
            self: for method chaining
        """

        self.request['dateRanges'] = [{
            'startDate': start_date,
            'endDate': end_date
        }]

        return self

    def add_dimensions(self, dimensions):
        """Add dimensions to request dictionary representation

        Args:
            `dimensions`    (list)  string list of dimension names

        Returns:
            self: for method chaining
        """

        self.request['dimensions'] += [
            {'name': _} for _ in dimensions
        ]

        return self

    def reset_dimensions(self):
        """Empty dimension vector

        Returns:
            self: for method chaining
        """

        self.request['dimensions'] = []

        return self

    def for_variables(self, variables):
        """Add variables to request dictionary representation

        Args:
            `variables`     (list)  string list of variable names

        Returns:
            self: for method chaining
        """

        self.request['metrics'] += [
            {'expression': _} for _ in variables
        ]

        return self

    def reset_variables(self):
        """Empty variable vector

        Returns:
            self: for method chaining
        """

        self.request['metrics'] = []

        return self

    def with_filter_clause(self, filter_clause):
        """Update filter

        Args:
            `filter_clause` (request_filter.RequestFilter) RequestFilter object

        Returns:
            self: for method chaining
        """

        self.request.update(filter_clause)

        return self

    def add_segment(self, segment):
        """Add segment to request

        Args:
            `segment`   (segment.Segment) Segment object

        Returns:
            self: for method chaining
        """

        self.request['segments'] += [segment]

        return self

    def run_request(self):
        """Query google analytics service and register response

        Returns:
            self: for method chaining
        """

        self.response = self.api.get_report(
            {
                "reportRequests": [self.request]
            }
        )

        return self

    def get_value(self, key):
        """Retrieve value for `key` in response

        Args:
            `key`   (str)   key, should be in [
                    'metrics', 'minimums', 'maximums'
                ]

        Returns:
            value associated to `key` in response
        """

        if key in ['metrics', 'minimums', 'maximums']:

            return self.response[
                'reports'
            ][0]['data']['rows'][0][key][0]['values']

        else:
            return ['wrong_key']

    def raw_data(self):
        """Returns raw response

        Returns:
            dict: raw google analytics api response
        """

        return self.response
