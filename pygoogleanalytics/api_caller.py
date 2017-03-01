# -*- coding: utf-8 -*-
"""api_caller module provides an APICaller class providing a wrapper for
building and requesting analytics object from google-api-python-client
"""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import httplib2


class APICaller(object):
    """APICaller class

    Provides a simple wrapper for building and requesting analytics object from
    google-api-python-client
    """

    def __init__(self, scopes, discovery_uri, key_file, service_account):
        """Initialize analytics object

        Args:
            `scopes`            (list)  list of scope strings
            `discovery_uri`     (tuple) tuple of uri strings
            `key_file`          (str)   path to p12 secret file
            `service_account`   (str)   service account address string
        """

        self.scopes = scopes
        self.discovery_uri = discovery_uri
        self.key_file = key_file
        self.service_account = service_account

        self.analytics = self.init_analytics()

    def init_analytics(self):
        """Initalize analytics variable

        Returns:
            A Resource object with methods for interacting with the service.
        """

        return build(
            'analytics',
            'v4',
            http=ServiceAccountCredentials.from_p12_keyfile(
                self.service_account,
                self.key_file,
                scopes=self.scopes
            ).authorize(httplib2.Http()),
            discoveryServiceUrl=self.discovery_uri
        )

    def get_report(self, request_body={}):
        """Emit a request to Google Analytics API service

        Args:
            `request_body`      (dict)  dictionary abstraction of request

        Returns:
            Response as string
        """

        return self.analytics.reports().batchGet(body=request_body).execute()
