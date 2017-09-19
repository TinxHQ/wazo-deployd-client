# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json

from wazo_deployd_client.command import DeploydCommand


class InstancesCommand(DeploydCommand):

    resource = 'tenants'
    _headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, client, tenant_uuid):
        self.tenant_uuid = tenant_uuid
        super().__init__(client)

    def list(self, provider_uuid=None):
        if provider_uuid:
            url = self._provider_instances_all_url(provider_uuid)
        elif not self.tenant_uuid:
            url = self._instances_all_no_tenant_url()
        else:
            url = self._instances_all_url()

        response = self.session.get(
            url,
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def _create_instance(self, url, instance_data):
        response = self.session.post(
            url,
            data=json.dumps(instance_data),
            headers=self._headers,
        )
        if response.status_code != 201:
            self.raise_from_response(response)

        return response.json()

    def register(self, instance_data):
        url = self._instances_all_url()
        return self._create_instance(url, instance_data)

    def create(self, provider_uuid, instance_data):
        url = self._provider_instances_all_url(provider_uuid)
        return self._create_instance(url, instance_data)

    def get(self, instance_uuid):
        response = self.session.get(
            self._instances_one_url(instance_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def get_wazo(self, instance_uuid):
        response = self.session.get(
            self._instances_wazo_url(instance_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def wizard(self, instance_uuid, wizard_data):
        response = self.session.post(
            self._instances_wizard_url(instance_uuid),
            data=json.dumps(wizard_data),
            headers=self._headers,
        )
        if response.status_code != 204:
            self.raise_from_response(response)

    def update(self, instance_uuid, instance_data):
        response = self.session.put(
            self._instances_one_url(instance_uuid),
            data=json.dumps(instance_data),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def _delete_instance(self, url):
        response = self.session.delete(url, headers=self._headers)
        if response.status_code != 204:
            self.raise_from_response(response)

    def unregister(self, instance_uuid):
        url = self._instances_one_url(instance_uuid)
        return self._delete_instance(url)

    def delete(self, provider_uuid, instance_uuid):
        url = self._provider_instances_one_url(
            instance_uuid,
            provider_uuid,
        )
        return self._delete_instance(url)

    def _instances_all_url(self):
        return '{base_url}/{tenant_uuid}/instances'.format(
            base_url=self.base_url,
            tenant_uuid=self.tenant_uuid,
        )

    def _instances_all_no_tenant_url(self):
        return '{base_url}/instances'.format(base_url=self._client.url())

    def _instances_one_url(self, instance_uuid):
        return '{base_url}/{instance_uuid}'.format(
            base_url=self._instances_all_url(),
            instance_uuid=instance_uuid,
        )

    def _instances_wazo_url(self, instance_uuid):
        return '{base_url}/wazo'.format(
            base_url=self._instances_one_url(instance_uuid),
        )

    def _instances_wizard_url(self, instance_uuid):
        return '{base_url}/wizard'.format(
            base_url=self._instances_wazo_url(instance_uuid),
        )

    def _provider_instances_all_url(self, provider_uuid):
        return '{base_url}/{tenant_uuid}/providers/{provider_uuid}/instances'.format(
            base_url=self.base_url,
            tenant_uuid=self.tenant_uuid,
            provider_uuid=provider_uuid,
        )

    def _provider_instances_one_url(self, instance_uuid, provider_uuid):
        return '{base_url}/{instance_uuid}'.format(
            base_url=self._provider_instances_all_url(provider_uuid),
            instance_uuid=instance_uuid,
        )
