# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_deployd_client.command import DeploydCommand


class StatusCommand(DeploydCommand):

    resource = 'status'

    def check(self):
        r = self.session.head(self.base_url, headers=self._ro_headers)
        if r.status_code != 200:
            self.raise_from_response(r)
