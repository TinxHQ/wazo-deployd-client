# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json

from wazo_deployd_client.command import DeploydCommand


class InstancesCommand(DeploydCommand):

    resource = 'instances'
    _headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, client):
        super().__init__(client)

    def list(self, provider_uuid=None, **params):
        if provider_uuid:
            url = self._provider_instances_all_url(provider_uuid)
        else:
            url = self._instances_all_url()

        response = self.session.get(
            url,
            headers=self._headers,
            params=params,
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

    def get_credential(self, instance_uuid, credential_uuid):
        url = self._credentials_one_url(instance_uuid, credential_uuid)
        response = self.session.get(url, headers=self._headers)
        if response.status_code != 200:
            self.raise_from_response(response)
        return response.json()

    def create_credential(self, instance_uuid, credential_data):
        url = self._credentials_all_url(instance_uuid)
        response = self.session.post(url, data=json.dumps(credential_data), headers=self._headers)
        if response.status_code != 201:
            self.raise_from_response(response)
        return response.json()

    def update_credential(self, instance_uuid, credential_uuid, credential_data):
        url = self._credentials_one_url(instance_uuid, credential_uuid)
        response = self.session.put(url, data=json.dumps(credential_data), headers=self._headers)
        if response.status_code != 200:
            self.raise_from_response(response)
        return response.json()

    def delete_credential(self, instance_uuid, credential_uuid):
        url = self._credentials_one_url(instance_uuid, credential_uuid)
        response = self.session.delete(url, headers=self._headers)
        if response.status_code != 204:
            self.raise_from_response(response)

    def _instances_all_url(self):
        return self.base_url

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

    def _credentials_one_url(self, instance_uuid, credential_uuid):
        return '{base_url}/{instance_uuid}/credentials/{credential_uuid}'.format(
            base_url=self._instances_all_url(),
            instance_uuid=instance_uuid,
            credential_uuid=credential_uuid,
        )

    def _credentials_all_url(self, instance_uuid):
        return '{base_url}/{instance_uuid}/credentials'.format(
            base_url=self._instances_all_url(),
            instance_uuid=instance_uuid,
        )

    def _provider_instances_all_url(self, provider_uuid):
        return self._client.url('providers', provider_uuid, 'instances')

    def _provider_instances_one_url(self, instance_uuid, provider_uuid):
        return '{base_url}/{instance_uuid}'.format(
            base_url=self._provider_instances_all_url(provider_uuid),
            instance_uuid=instance_uuid,
        )


class TenantAwareInstancesCommand(InstancesCommand):
    def __init__(self, client, tenant_uuids):
        super().__init__(client)
        self._headers['Wazo-Tenant'] = ', '.join(tenant_uuids)
