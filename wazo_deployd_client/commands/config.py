# Copyright 2017-2019 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_deployd_client.command import DeploydCommand


class ConfigCommand(DeploydCommand):

    resource = 'config'

    def get(self):
        r = self.session.get(self.base_url, headers=self._headers)
        self.raise_from_response(r)
        return r.json()
