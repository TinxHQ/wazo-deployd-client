# wazo-deployd-client

A python client library to access wazo-deployd

## Usage

### Creating a client

```python
from wazo_deployd_client import Client
client = Client('localhost', verify_certificate=False)
```

## Config

```python
client.config()
```

## Providers

### List providers

```python
client.tenant(tenant_uuid).providers.list()
```

### Create a provider

```python
client.tenant(tenant_uuid).providers.create(provider_data)
```

### Get a provider

```python
client.tenant(tenant_uuid).providers.get(provider_uuid)
```

### Update a provider

```python
client.tenant(tenant_uuid).providers.update(provider_uuid, provider_data)
```

### Delete a provider

```python
client.tenant(tenant_uuid).providers.delete(provider_uuid)
```

## Instances

### List instances

```python
client.tenant(tenant_uuid).instances.list()

# List by provider
client.tenant(tenant_uuid).instances.list(provider_uuid=provider_uuid)
```

### Create an instance

```python
client.tenant(tenant_uuid).instances.create(provider_uuid, instance_data)
```

### Register an instance

```python
client.tenant(tenant_uuid).instances.register(instance_data)
```

### Get an instance

```python
client.tenant(tenant_uuid).instances.get(instance_uuid)
```

### Get an instance wazo

```python
client.tenant(tenant_uuid).instances.get_wazo(instance_uuid)
```

### Update an instance

```python
client.tenant(tenant_uuid).instances.update(instance_uuid, instance_data)
```

### Delete an instance

```python
client.tenant(tenant_uuid).instances.delete(provider_uuid, instance_uuid)
```

### Unregister an instance

```python
client.tenant(tenant_uuid).instances.unregister(instance_uuid)
```

## Debian package

Follow the following steps to build a debian package for wazo-deployd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-deployd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
