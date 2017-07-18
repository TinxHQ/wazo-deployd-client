# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from xivo_lib_rest_client.client import BaseClient


class DeploydClient(BaseClient):

    namespace = 'wazo_deployd_client.commands'

    def __init__(self,
                 host,
                 port=9800,
                 version='0.1',
                 **kwargs):
        super(DeploydClient, self).__init__(
              host=host,
              port=port,
              version=version,
              **kwargs)