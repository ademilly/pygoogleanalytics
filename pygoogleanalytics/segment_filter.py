# -*- coding: utf-8 -*-
"""segment_filter module provides SegmentFilter class handling segment filters

Filters added to segments should be represented as python dict
Example:
    - {
        "metricFilter": {
            "scope": "SESSION",
            "metricName": "ga:pageviews",
            "operator": "GREATER_THAN",
            "comparisonValue": "1"
        }
    }

More details available in google analytics API python documentation
or at https://developers.google.com/analytics/devguides/reporting/core/v4/
"""


class SegmentFilter(dict):
    """SegmentFilter class provides method to handle filter clause
    """

    def __init__(self):
        """Initialize SegmentFilter object
        """

        self['segmentFilterClauses'] = []

    def add_filter(self, filter_clause):
        """Add filter

        Args:
            `filter_clause` (dict)  dict representation of filter

        Returns:
            self: for method chaining
        """

        self['segmentFilterClauses'] += [filter_clause]

        return self

    def reset_filters(self):
        """Reset filters

        Returns:
            self: for method chaining
        """

        self['segmentFilterClauses'] = []

        return self
