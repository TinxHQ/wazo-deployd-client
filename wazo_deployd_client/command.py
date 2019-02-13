# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import DeploydError
from .exceptions import DeploydServiceUnavailable
from .exceptions import InvalidDeploydError


class DeploydCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise DeploydServiceUnavailable(response)

        try:
            raise DeploydError(response)
        except InvalidDeploydError:
            RESTCommand.raise_from_response(response)
