# -*- coding: utf-8 -*-
"""request_filter module provides a RequestFilter class providing an
abstraction for google analytics API request filters handling
"""


class RequestFilter(dict):
    """RequestFilter class

    Provides an abstraction for filter writing in google analytics API
    """

    def __init__(self, operator):
        """Initialize RequestFilter object

        Args:
            `operator`  (str)   string representing operator linking filters
                should be in ['or', 'and']
        """

        self['dimensionFilterClauses'] = [
            {
                "operator": operator.upper(),
                "filters": []
            }
        ]

    def add_filter(self, dimension_filter):
        """Add a new filter

        Args:
            `dimension_filter`  (dict)  dictionary representation of
                dimension filter syntax from google analytics API
                dimension_filters.keys() should be equal to [
                    'dimensionName', 'operator', 'expressions'
                ]

        Returns:
            RequestFilter: self for method chaining
        """

        self['dimensionFilterClauses'][0]['filters'] += [dimension_filter]

        return self

    def reset_filters(self):
        """Erase saved filters

        Returns:
            RequestFilter: self for method chaining
        """

        self['dimensionFilterClauses'][0]['filters'] = []

        return self

    def set_operator(self, operator):
        """Set operator linking filters

        Args:
            `operator`  (str)   string representing operator linking filters
                should be in ['or', 'and']

        Returns:
            RequestFilter: self for method chaining
        """

        self['dimensionFilterClauses']['operator'] = operator.upper()

        return self
