# wazo-webhookd-client

A python client library to access wazo-webhookd

## Usage

### Creating a client

```python
from wazo_webhookd_client import Client
client = Client('localhost', verify_certificate=False, token=<xivo-auth-token>)
```

### Getting the service configuration

```python
client.config()
```

## Debian package

Follow the following steps to build a debian package for wazo-webhookd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-webhookd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
