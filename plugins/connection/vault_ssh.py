# Copyright: (c) 2026, Clément (Cleymax) Perrin <github@clementperrin.fr>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
name: vault_ssh
short_description: SSH connection plugin with HashiCorp Vault credential retrieval
description:
  - This connection plugin extends the standard C(ssh) plugin to retrieve SSH credentials
    from HashiCorp Vault.
  - It supports C(token), C(approle) and C(jwt) authentication methods, KV v1 and v2
    secret engines.
  - It allows dynamic resolution of the Vault secret path using simple placeholders
    C({host}), C({inventory_hostname}) and C({user}).
  - The plugin caches Vault secrets in memory for a configurable duration to reduce
    load on the Vault server.
author:
  - Clément Perrin (@cleymax)
options:
  vault_enabled:
    description:
      - Globally enable or disable the Vault credential lookup.
      - When disabled the plugin behaves exactly like the standard C(ssh) plugin.
    type: bool
    default: true
    env:
      - name: ANSIBLE_VAULT_SSH_ENABLED
    ini:
      - section: vault_ssh_connection
        key: enabled
    vars:
      - name: ansible_vault_ssh_enabled
  vault_url:
    description:
      - URL of the HashiCorp Vault server (e.g. C(https://vault.example.com:8200)).
    type: string
    required: true
    env:
      - name: VAULT_ADDR
      - name: ANSIBLE_HASHI_VAULT_ADDR
    ini:
      - section: vault_ssh_connection
        key: url
    vars:
      - name: ansible_vault_url
      - name: vault_url
  vault_namespace:
    description:
      - Vault Enterprise namespace (e.g. C(admin/team-a)).
    type: string
    env:
      - name: VAULT_NAMESPACE
      - name: ANSIBLE_HASHI_VAULT_NAMESPACE
    ini:
      - section: vault_ssh_connection
        key: namespace
    vars:
      - name: ansible_vault_namespace
      - name: vault_namespace
  vault_auth_method:
    description:
      - Authentication method used against Vault.
      - C(approle) uses C(vault_role_id) / C(vault_secret_id).
      - C(jwt) uses C(vault_jwt) / C(vault_jwt_path) with C(vault_role).
      - C(token) uses C(vault_token) directly.
    type: string
    choices:
      - approle
      - jwt
      - token
    default: token
    env:
      - name: ANSIBLE_VAULT_AUTH_METHOD
    ini:
      - section: vault_ssh_connection
        key: auth_method
    vars:
      - name: ansible_vault_auth_method
      - name: vault_auth_method
  vault_token:
    description:
      - Vault token used when C(vault_auth_method=token).
    type: string
    env:
      - name: VAULT_TOKEN
      - name: ANSIBLE_HASHI_VAULT_TOKEN
    vars:
      - name: ansible_vault_token
      - name: vault_token
  vault_token_file:
    description:
      - Path to a file containing a Vault token (e.g. C(~/.vault-token)).
      - Used as a fallback when C(vault_token) is not set.
    type: string
    default: ~/.vault-token
    env:
      - name: ANSIBLE_VAULT_TOKEN_FILE
    ini:
      - section: vault_ssh_connection
        key: token_file
    vars:
      - name: ansible_vault_token_file
  vault_role_id:
    description:
      - AppRole RoleID used when C(vault_auth_method=approle).
    type: string
    env:
      - name: VAULT_ROLE_ID
      - name: ANSIBLE_HASHI_VAULT_ROLE_ID
    vars:
      - name: ansible_vault_role_id
      - name: vault_role_id
  vault_secret_id:
    description:
      - AppRole SecretID used when C(vault_auth_method=approle).
    type: string
    env:
      - name: VAULT_SECRET_ID
      - name: ANSIBLE_HASHI_VAULT_SECRET_ID
    vars:
      - name: ansible_vault_secret_id
      - name: vault_secret_id
  vault_approle_mount_point:
    description:
      - Mount point of the AppRole auth backend.
    type: string
    default: approle
    env:
      - name: ANSIBLE_VAULT_APPROLE_MOUNT
    ini:
      - section: vault_ssh_connection
        key: approle_mount_point
    vars:
      - name: ansible_vault_approle_mount_point
  vault_jwt:
    description:
      - The signed JWT/OIDC token used when C(vault_auth_method=jwt).
      - If not provided, the plugin will try to read C(vault_jwt_path).
    type: string
    env:
      - name: VAULT_JWT
      - name: ANSIBLE_VAULT_JWT
    vars:
      - name: ansible_vault_jwt
      - name: vault_jwt
  vault_jwt_path:
    description:
      - Path to a file containing the JWT (e.g. Kubernetes service account token).
    type: string
    default: /var/run/secrets/kubernetes.io/serviceaccount/token
    env:
      - name: ANSIBLE_VAULT_JWT_PATH
    ini:
      - section: vault_ssh_connection
        key: jwt_path
    vars:
      - name: ansible_vault_jwt_path
  vault_role:
    description:
      - Vault role name to use with the JWT auth method.
    type: string
    env:
      - name: VAULT_ROLE
      - name: ANSIBLE_VAULT_ROLE
    vars:
      - name: ansible_vault_role
      - name: vault_role
  vault_jwt_mount_point:
    description:
      - Mount point of the JWT/OIDC auth backend.
    type: string
    default: jwt
    env:
      - name: ANSIBLE_VAULT_JWT_MOUNT
    ini:
      - section: vault_ssh_connection
        key: jwt_mount_point
    vars:
      - name: ansible_vault_jwt_mount_point
  vault_secret_path:
    description:
      - Path of the secret inside the KV engine, relative to the mount point.
      - Supports Jinja-free simple placeholders C({host}), C({inventory_hostname}) and
        C({user}).
      - Example C(hosts/{host}) or C(linux/{inventory_hostname}).
    type: string
    required: true
    env:
      - name: ANSIBLE_VAULT_SECRET_PATH
    ini:
      - section: vault_ssh_connection
        key: secret_path
    vars:
      - name: ansible_vault_secret_path
      - name: vault_secret_path
  vault_mount_point:
    description:
      - Mount point of the KV secret engine.
    type: string
    default: secret
    env:
      - name: ANSIBLE_VAULT_MOUNT_POINT
    ini:
      - section: vault_ssh_connection
        key: mount_point
    vars:
      - name: ansible_vault_mount_point
      - name: vault_mount_point
  vault_kv_version:
    description:
      - Version of the KV secret engine.
    type: string
    choices:
      - "1"
      - "2"
    default: "2"
    env:
      - name: ANSIBLE_VAULT_KV_VERSION
    ini:
      - section: vault_ssh_connection
        key: kv_version
    vars:
      - name: ansible_vault_kv_version
  vault_key_username:
    description: Key inside the Vault secret holding the SSH username.
    type: string
    default: username
    ini:
      - section: vault_ssh_connection
        key: key_username
    vars:
      - name: ansible_vault_key_username
  vault_key_password:
    description: Key inside the Vault secret holding the SSH password.
    type: string
    default: password
    ini:
      - section: vault_ssh_connection
        key: key_password
    vars:
      - name: ansible_vault_key_password
  vault_key_become_password:
    description: Key inside the Vault secret holding the privilege escalation password.
    type: string
    default: become_password
    ini:
      - section: vault_ssh_connection
        key: key_become_password
    vars:
      - name: ansible_vault_key_become_password
  vault_key_private_key:
    description: Key inside the Vault secret holding the SSH private key (PEM content).
    type: string
    default: private_key
    ini:
      - section: vault_ssh_connection
        key: key_private_key
    vars:
      - name: ansible_vault_key_private_key
  vault_key_passphrase:
    description:
      - Key inside the Vault secret holding the private key passphrase.
      - When set, the plugin uses C(sshpass -P 'Enter passphrase') behaviour via ssh-agent
        free flow.
    type: string
    default: private_key_passphrase
    ini:
      - section: vault_ssh_connection
        key: key_passphrase
    vars:
      - name: ansible_vault_key_passphrase
  vault_verify:
    description:
      - Whether to verify the Vault server TLS certificate.
      - Can also be a path to a CA bundle.
    type: string
    default: "true"
    env:
      - name: VAULT_SKIP_VERIFY_INVERTED
      - name: ANSIBLE_VAULT_VERIFY
    ini:
      - section: vault_ssh_connection
        key: verify
    vars:
      - name: ansible_vault_verify
      - name: vault_verify
  vault_ca_cert:
    description: Path to a CA bundle used to verify the Vault TLS certificate.
    type: string
    env:
      - name: VAULT_CACERT
    ini:
      - section: vault_ssh_connection
        key: ca_cert
    vars:
      - name: ansible_vault_ca_cert
  vault_client_cert:
    description: Path to a client certificate for Vault mTLS.
    type: string
    env:
      - name: VAULT_CLIENT_CERT
    vars:
      - name: ansible_vault_client_cert
  vault_client_key:
    description: Path to the client certificate key for Vault mTLS.
    type: string
    env:
      - name: VAULT_CLIENT_KEY
    vars:
      - name: ansible_vault_client_key
  vault_timeout:
    description: Timeout (seconds) for HTTP requests to Vault.
    type: int
    default: 30
    env:
      - name: ANSIBLE_VAULT_TIMEOUT
    ini:
      - section: vault_ssh_connection
        key: timeout
    vars:
      - name: ansible_vault_timeout
  vault_prefer_static:
    description:
      - When C(true), any credential already defined in the inventory / AAP credential
        takes precedence over the value retrieved from Vault.
      - When C(false) (default), Vault wins.
    type: bool
    default: false
    ini:
      - section: vault_ssh_connection
        key: prefer_static
    vars:
      - name: ansible_vault_prefer_static
  vault_fail_on_missing:
    description:
      - Fail the connection when the Vault secret cannot be retrieved.
      - When C(false), the plugin logs a warning and falls back to standard SSH behaviour.
    type: bool
    default: true
    ini:
      - section: vault_ssh_connection
        key: fail_on_missing
    vars:
      - name: ansible_vault_fail_on_missing
  vault_cache_ttl:
    description:
      - Number of seconds a Vault secret is cached in memory (per worker process).
      - Set to C(0) to disable caching.
    type: int
    default: 300
    ini:
      - section: vault_ssh_connection
        key: cache_ttl
    vars:
      - name: ansible_vault_cache_ttl
'''

import yaml
from ansible.plugins.connection.ssh import DOCUMENTATION as SSH_DOCUMENTATION

_base = yaml.safe_load(SSH_DOCUMENTATION)
_ours = yaml.safe_load(DOCUMENTATION)
_base['options'].update(_ours['options'])
_base['name'] = _ours['name']
_base['short_description'] = _ours['short_description']
_base['description'] = _ours['description']
_base['author'] = _ours['author']
_base['version_added'] = _ours['version_added']
DOCUMENTATION = yaml.dump(_base, default_flow_style=False, sort_keys=False)


EXAMPLES = r'''
# ---------------------------------------------------------------------------
# inventory/hosts.yml - AppRole authentication, KV v2
# ---------------------------------------------------------------------------
all:
  vars:
    ansible_connection: cleymax.ansible_global_collection.vault_ssh
    vault_url: https://vault.example.com:8200
    vault_auth_method: approle
    vault_role_id: "{{ lookup('env', 'VAULT_ROLE_ID') }}"
    vault_secret_id: "{{ lookup('env', 'VAULT_SECRET_ID') }}"
    vault_mount_point: secret
    vault_secret_path: "ansible/hosts/{inventory_hostname}"
  hosts:
    server01.example.com:
    server02.example.com:

# ---------------------------------------------------------------------------
# JWT authentication (Kubernetes / AAP OIDC)
# ---------------------------------------------------------------------------
test:
  vars:
    ansible_connection: cleymax.ansible_global_collection.vault_ssh
    vault_url: https://vault.example.com:8200
    vault_auth_method: jwt
    vault_role: ansible-automation
    vault_jwt_mount_point: jwt
    vault_jwt_path: /var/run/secrets/kubernetes.io/serviceaccount/token
    vault_secret_path: "ansible/linux/{host}"

# ---------------------------------------------------------------------------
# Token authentication with a per-group secret path
# ---------------------------------------------------------------------------
webservers:
  vars:
    ansible_connection: cleymax.ansible_global_collection.vault_ssh
    vault_auth_method: token
    vault_token: "{{ lookup('env', 'VAULT_TOKEN') }}"
    vault_secret_path: "ansible/webservers/common"
    vault_key_username: ssh_user
    vault_key_password: ssh_pass
    vault_key_become_password: sudo_pass
'''

import atexit
import errno
import os
import stat
import tempfile
import time

from ansible.errors import AnsibleConnectionFailure, AnsibleError
from ansible.module_utils.common.text.converters import to_bytes, to_native, to_text
from ansible.plugins.connection.ssh import Connection as SSHConnection
from ansible.utils.display import Display

display = Display()

try:
    import hvac
    from hvac.exceptions import VaultError

    HAS_HVAC = True
    HVAC_IMPORT_ERROR = None
except ImportError as _imp_exc:  # pragma: no cover
    HAS_HVAC = False
    HVAC_IMPORT_ERROR = _imp_exc
    VaultError = Exception  # type: ignore


# ---------------------------------------------------------------------------
# Process wide cache: {cache_key: (expiry_epoch, secret_dict)}
# Each AAP/AWX forked worker gets its own copy which keeps Vault load low
# while never sharing secrets across processes.
# ---------------------------------------------------------------------------
_SECRET_CACHE = {}
_CLIENT_CACHE = {}


def _now():
    return time.time()


class Connection(SSHConnection):
    """SSH based connection plugin that resolves credentials from HashiCorp Vault."""

    transport = 'vault_ssh'
    has_pipelining = True

    def __init__(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)
        self._vault_resolved = False
        self._vault_tmp_key_file = None
        self._vault_secret = {}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _opt(self, name, default=None):
        """Safe get_option wrapper (option may not exist on older cores)."""
        try:
            value = self.get_option(name)
        except (KeyError, AttributeError):
            return default
        return default if value is None else value

    def _bool(self, name, default=False):
        value = self._opt(name, default)
        if isinstance(value, bool):
            return value
        return to_text(value).strip().lower() in ('1', 'true', 'yes', 'on')

    def _render_path(self, template):
        """Replace simple placeholders in the Vault secret path."""
        host = self._opt('host') or self.host or ''
        user = self._opt('remote_user') or ''
        inventory_hostname = ''
        try:
            inventory_hostname = to_text(
                self._play_context.remote_addr or host)
        except Exception:
            inventory_hostname = host

        mapping = {
            '{host}': to_text(host),
            '{hostname}': to_text(host),
            '{inventory_hostname}': to_text(inventory_hostname),
            '{user}': to_text(user),
            '{remote_user}': to_text(user),
        }
        rendered = to_text(template)
        for key, value in mapping.items():
            rendered = rendered.replace(key, value)
        return rendered.strip('/')

    # ------------------------------------------------------------------
    # Vault client construction & authentication
    # ------------------------------------------------------------------
    def _resolve_verify(self):
        ca_cert = self._opt('vault_ca_cert')
        if ca_cert:
            return ca_cert

        verify = self._opt('vault_verify', 'true')
        if isinstance(verify, bool):
            return verify

        verify_text = to_text(verify).strip()
        if verify_text.lower() in ('1', 'true', 'yes', 'on'):
            return True
        if verify_text.lower() in ('0', 'false', 'no', 'off'):
            return False
        # Assume it is a path to a CA bundle
        return verify_text

    def _client_cert_tuple(self):
        cert = self._opt('vault_client_cert')
        key = self._opt('vault_client_key')
        if cert and key:
            return (cert, key)
        if cert:
            return cert
        return None

    def _build_client(self):
        if not HAS_HVAC:
            raise AnsibleConnectionFailure(
                "The 'hvac' Python library is required by the vault_ssh connection "
                "plugin but could not be imported: %s. Install it with "
                "'pip install hvac' inside your execution environment."
                % to_native(HVAC_IMPORT_ERROR)
            )

        url = self._opt('vault_url')
        if not url:
            raise AnsibleConnectionFailure(
                "vault_url (or VAULT_ADDR) must be defined for the vault_ssh connection plugin."
            )

        namespace = self._opt('vault_namespace') or None
        auth_method = to_text(self._opt('vault_auth_method', 'token')).lower()

        # Cache key must include everything that changes the identity of the client
        cache_key = (url, namespace, auth_method,
                     self._opt('vault_role_id'),
                     self._opt('vault_role'),
                     self._opt('vault_approle_mount_point'),
                     self._opt('vault_jwt_mount_point'))

        cached = _CLIENT_CACHE.get(cache_key)
        if cached is not None:
            client, expires = cached
            if expires == 0 or expires > _now():
                try:
                    if client.is_authenticated():
                        return client
                except Exception:
                    pass
            _CLIENT_CACHE.pop(cache_key, None)

        client_kwargs = {
            'url': url,
            'verify': self._resolve_verify(),
            'timeout': int(self._opt('vault_timeout', 30)),
        }
        if namespace:
            client_kwargs['namespace'] = namespace
        cert = self._client_cert_tuple()
        if cert:
            client_kwargs['cert'] = cert

        client = hvac.Client(**client_kwargs)

        lease_duration = 0
        try:
            if auth_method == 'token':
                lease_duration = self._auth_token(client)
            elif auth_method == 'approle':
                lease_duration = self._auth_approle(client)
            elif auth_method == 'jwt':
                lease_duration = self._auth_jwt(client)
            else:
                raise AnsibleConnectionFailure(
                    "Unsupported vault_auth_method '%s'. Supported: approle, jwt, token."
                    % auth_method
                )
        except AnsibleError:
            raise
        except VaultError as exc:
            raise AnsibleConnectionFailure(
                "Vault authentication with method '%s' failed: %s" % (
                    auth_method, to_native(exc))
            )
        except Exception as exc:
            raise AnsibleConnectionFailure(
                "Unexpected error while authenticating to Vault (%s): %s"
                % (auth_method, to_native(exc))
            )

        if not client.is_authenticated():
            raise AnsibleConnectionFailure(
                "Vault client is not authenticated after using the '%s' method." % auth_method
            )

        # Renew the client slightly before the token actually expires
        expires = 0
        if lease_duration:
            expires = _now() + max(int(lease_duration) * 0.8, 30)
        _CLIENT_CACHE[cache_key] = (client, expires)

        display.vvv(u"vault_ssh: authenticated to Vault at %s using '%s'" % (url, auth_method),
                    host=self.host)
        return client

    def _auth_token(self, client):
        token = self._opt('vault_token')

        if not token:
            token_file = self._opt('vault_token_file', '~/.vault-token')
            if token_file:
                token_file = os.path.expanduser(
                    os.path.expandvars(to_text(token_file)))
                if os.path.isfile(token_file):
                    try:
                        with open(token_file, 'rb') as fh:
                            token = to_text(fh.read()).strip()
                    except (IOError, OSError) as exc:
                        display.warning(
                            u"vault_ssh: unable to read token file %s: %s"
                            % (token_file, to_text(exc))
                        )

        if not token:
            raise AnsibleConnectionFailure(
                "vault_auth_method is 'token' but no token was found "
                "(vault_token / VAULT_TOKEN / vault_token_file)."
            )

        client.token = to_native(token)

        # Best effort lease duration lookup so we can cache the client
        try:
            info = client.auth.token.lookup_self()
            return int(info.get('data', {}).get('ttl', 0) or 0)
        except Exception:
            return 0

    def _auth_approle(self, client):
        role_id = self._opt('vault_role_id')
        secret_id = self._opt('vault_secret_id')

        if not role_id:
            raise AnsibleConnectionFailure(
                "vault_auth_method is 'approle' but vault_role_id is not defined."
            )

        kwargs = {
            'role_id': to_native(role_id),
            'mount_point': to_native(self._opt('vault_approle_mount_point', 'approle')),
        }
        if secret_id:
            kwargs['secret_id'] = to_native(secret_id)

        response = client.auth.approle.login(**kwargs)
        auth = response.get('auth', {}) if isinstance(response, dict) else {}
        if auth.get('client_token'):
            client.token = auth['client_token']
        return int(auth.get('lease_duration', 0) or 0)

    def _auth_jwt(self, client):
        jwt = self._opt('vault_jwt')

        if not jwt:
            jwt_path = self._opt('vault_jwt_path')
            if jwt_path:
                jwt_path = os.path.expanduser(
                    os.path.expandvars(to_text(jwt_path)))
                if os.path.isfile(jwt_path):
                    try:
                        with open(jwt_path, 'rb') as fh:
                            jwt = to_text(fh.read()).strip()
                    except (IOError, OSError) as exc:
                        raise AnsibleConnectionFailure(
                            "Unable to read JWT from %s: %s" % (
                                jwt_path, to_native(exc))
                        )

        if not jwt:
            raise AnsibleConnectionFailure(
                "vault_auth_method is 'jwt' but no JWT was provided "
                "(vault_jwt / VAULT_JWT / vault_jwt_path)."
            )

        role = self._opt('vault_role')
        mount_point = to_native(self._opt('vault_jwt_mount_point', 'jwt'))

        # hvac >= 0.10 exposes client.auth.jwt, older releases only have the
        # generic login endpoint - handle both for maximum compatibility.
        response = None
        try:
            response = client.auth.jwt.jwt_login(
                role=to_native(role) if role else None,
                jwt=to_native(jwt),
                path=mount_point,
            )
        except AttributeError:
            payload = {'jwt': to_native(jwt)}
            if role:
                payload['role'] = to_native(role)
            response = client.auth_cubbyhole if False else client.login(
                '/v1/auth/%s/login' % mount_point, json=payload
            )

        auth = response.get('auth', {}) if isinstance(response, dict) else {}
        if auth.get('client_token'):
            client.token = auth['client_token']
        return int(auth.get('lease_duration', 0) or 0)

    # ------------------------------------------------------------------
    # Secret retrieval
    # ------------------------------------------------------------------
    def _read_secret(self, client, mount_point, path, kv_version):
        try:
            if to_text(kv_version) == '1':
                response = client.secrets.kv.v1.read_secret(
                    path=path, mount_point=mount_point
                )
                return response.get('data', {}) or {}

            response = client.secrets.kv.v2.read_secret_version(
                path=path, mount_point=mount_point, raise_on_deleted_version=True
            )
            return (response.get('data', {}) or {}).get('data', {}) or {}
        except TypeError:
            # Older hvac releases do not accept raise_on_deleted_version
            response = client.secrets.kv.v2.read_secret_version(
                path=path, mount_point=mount_point
            )
            return (response.get('data', {}) or {}).get('data', {}) or {}

    def _fetch_credentials(self):
        mount_point = to_text(
            self._opt('vault_mount_point', 'secret')).strip('/')
        kv_version = to_text(self._opt('vault_kv_version', '2'))
        raw_path = self._opt('vault_secret_path')

        if not raw_path:
            raise AnsibleConnectionFailure(
                "vault_secret_path must be defined for the vault_ssh connection plugin."
            )

        path = self._render_path(raw_path)
        url = self._opt('vault_url')
        namespace = self._opt('vault_namespace') or ''

        cache_ttl = int(self._opt('vault_cache_ttl', 300) or 0)
        cache_key = (url, namespace, mount_point, kv_version, path)

        if cache_ttl > 0:
            entry = _SECRET_CACHE.get(cache_key)
            if entry and entry[0] > _now():
                display.vvvv(u"vault_ssh: using cached secret for %s/%s" % (mount_point, path),
                             host=self.host)
                return entry[1]

        client = self._build_client()

        display.vvv(u"vault_ssh: reading secret kv%s://%s/%s" % (kv_version, mount_point, path),
                    host=self.host)

        try:
            secret = self._read_secret(client, mount_point, path, kv_version)
        except VaultError as exc:
            raise AnsibleConnectionFailure(
                "Unable to read Vault secret '%s' from mount '%s': %s"
                % (path, mount_point, to_native(exc))
            )
        except Exception as exc:
            raise AnsibleConnectionFailure(
                "Unexpected error while reading Vault secret '%s': %s" % (
                    path, to_native(exc))
            )

        if not isinstance(secret, dict):
            secret = {}

        if cache_ttl > 0:
            _SECRET_CACHE[cache_key] = (_now() + cache_ttl, secret)

        return secret

    # ------------------------------------------------------------------
    # Private key handling
    # ------------------------------------------------------------------
    def _write_private_key(self, key_material):
        """Write the PEM private key to a 0600 temp file and return its path."""
        key_text = to_text(key_material, errors='surrogate_or_strict')

        # Normalise escaped newlines that are common when secrets are stored
        # through the Vault UI / JSON payloads.
        if '\\n' in key_text and '\n' not in key_text.strip():
            key_text = key_text.replace('\\n', '\n')
        if not key_text.endswith('\n'):
            key_text += '\n'

        tmp_dir = os.environ.get('ANSIBLE_LOCAL_TEMP') or tempfile.gettempdir()
        fd, path = tempfile.mkstemp(
            prefix='.vault_ssh_key_', suffix='.pem', dir=tmp_dir)
        try:
            os.fchmod(fd, stat.S_IRUSR | stat.S_IWUSR)  # 0600
            with os.fdopen(fd, 'wb') as fh:
                fh.write(to_bytes(key_text, errors='surrogate_or_strict'))
        except Exception:
            try:
                os.close(fd)
            except OSError:
                pass
            self._safe_unlink(path)
            raise

        display.vvvv(u"vault_ssh: wrote temporary private key to %s" %
                     path, host=self.host)

        atexit.register(self._safe_unlink, path)
        return path

    @staticmethod
    def _safe_unlink(path):
        if not path:
            return
        try:
            os.unlink(path)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                display.warning(
                    u"vault_ssh: could not remove %s: %s" % (path, to_text(exc)))

    # ------------------------------------------------------------------
    # Credential injection
    # ------------------------------------------------------------------
    def _apply_credentials(self, secret):
        prefer_static = self._bool('vault_prefer_static', False)

        k_user = self._opt('vault_key_username', 'username')
        k_pass = self._opt('vault_key_password', 'password')
        k_become = self._opt('vault_key_become_password', 'become_password')
        k_key = self._opt('vault_key_private_key', 'private_key')

        def _pick(key):
            if not key:
                return None
            value = secret.get(key)
            if value in (None, ''):
                return None
            return value

        # ---- remote user -------------------------------------------------
        username = _pick(k_user)
        if username:
            current = self._opt('remote_user')
            if not (prefer_static and current):
                self.set_option('remote_user', to_text(username))
                try:
                    self._play_context.remote_user = to_text(username)
                except Exception:
                    pass
                display.vvv(
                    u"vault_ssh: remote_user set from Vault", host=self.host)

        # ---- ssh password ------------------------------------------------
        password = _pick(k_pass)
        if password:
            current = self._opt('password')
            if not (prefer_static and current):
                self.set_option('password', to_text(password))
                try:
                    self._play_context.password = to_text(password)
                except Exception:
                    pass
                display.vvv(
                    u"vault_ssh: ssh password set from Vault", host=self.host)

        # ---- become password ---------------------------------------------
        become_password = _pick(k_become)
        if become_password:
            become_password = to_text(become_password)
            pc = self._play_context
            current = getattr(pc, 'become_pass', None)
            if not (prefer_static and current):
                try:
                    pc.become_pass = become_password
                except Exception:
                    pass
                # Newer cores read the become password from the become plugin
                become_plugin = getattr(self, 'become', None)
                if become_plugin is not None:
                    try:
                        become_plugin.set_options(
                            direct={'become_pass': become_password})
                    except Exception:
                        try:
                            become_plugin._become_pass = become_password
                        except Exception:
                            pass
                display.vvv(
                    u"vault_ssh: become password set from Vault", host=self.host)

        # ---- private key --------------------------------------------------
        private_key = _pick(k_key)
        if private_key:
            current = self._opt('private_key_file')
            if not (prefer_static and current):
                self._vault_tmp_key_file = self._write_private_key(private_key)
                self.set_option('private_key_file', self._vault_tmp_key_file)
                try:
                    self._play_context.private_key_file = self._vault_tmp_key_file
                except Exception:
                    pass
                display.vvv(
                    u"vault_ssh: private key retrieved from Vault", host=self.host)

        if not any([username, password, become_password, private_key]):
            display.warning(
                u"vault_ssh: the Vault secret did not contain any of the expected keys "
                u"(%s, %s, %s, %s) for host %s"
                % (k_user, k_pass, k_become, k_key, self.host)
            )

    def _resolve_vault_credentials(self):
        if self._vault_resolved:
            return
        self._vault_resolved = True

        if not self._bool('vault_enabled', True):
            display.vvv(u"vault_ssh: Vault lookup disabled, behaving like plain ssh",
                        host=self.host)
            return

        fail_on_missing = self._bool('vault_fail_on_missing', True)

        try:
            secret = self._fetch_credentials()
        except AnsibleConnectionFailure:
            if fail_on_missing:
                raise
            display.warning(
                u"vault_ssh: credential retrieval failed for host %s, falling back to "
                u"statically defined credentials (vault_fail_on_missing=false)." % self.host
            )
            self._vault_secret = {}
            return
        except Exception as exc:
            if fail_on_missing:
                raise AnsibleConnectionFailure(
                    "vault_ssh: unexpected error retrieving credentials for %s: %s"
                    % (self.host, to_native(exc))
                )
            display.warning(
                u"vault_ssh: unexpected error retrieving credentials for %s: %s (ignored)"
                % (self.host, to_text(exc))
            )
            self._vault_secret = {}
            return

        self._vault_secret = secret or {}
        self._apply_credentials(self._vault_secret)

    def _connect(self):
        """Resolve Vault credentials before the parent builds the ssh command."""
        if not self._connected:
            self._resolve_vault_credentials()
        return super(Connection, self)._connect()

    def reset(self):
        """Close the control socket and force credential re-resolution."""
        try:
            super(Connection, self).reset()
        except Exception as exc:
            display.warning(
                u"vault_ssh: error during connection reset for %s: %s"
                % (self.host, to_text(exc))
            )
            raise
        finally:
            self._cleanup_key_file()
            self._vault_resolved = False
            self._connected = False

    def close(self):
        """Tear down and invalidate cached credential state."""
        try:
            super(Connection, self).close()
        finally:
            self._cleanup_key_file()
            self._vault_resolved = False

    def _cleanup_key_file(self):
        if self._vault_tmp_key_file:
            self._safe_unlink(self._vault_tmp_key_file)
            self._vault_tmp_key_file = None
