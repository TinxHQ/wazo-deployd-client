# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class DeploydError(HTTPError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidDeploydError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
            if body.get('resource', None):
                self.resource = body['resource']
        except KeyError:
            raise InvalidDeploydError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super().__init__(exception_message, response=response)


class DeploydServiceUnavailable(DeploydError):
    pass


class InvalidDeploydError(Exception):
    pass
