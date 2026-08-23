.. Created with antsibull-docs 2.26.0

cleymax.ansible_global_collection.vault_ssh connection -- SSH connection plugin with HashiCorp Vault credential retrieval
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This connection plugin is part of the `cleymax.ansible_global_collection collection <https://galaxy.ansible.com/ui/repo/published/cleymax/ansible_global_collection/>`_ (version 1.0.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible\-galaxy collection install cleymax.ansible\_global\_collection`.

To use it in a playbook, specify: ``cleymax.ansible_global_collection.vault_ssh``.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This connection plugin extends the standard :literal:`ssh` plugin to retrieve SSH credentials from HashiCorp Vault.
- It supports :literal:`token`\ , :literal:`approle` and :literal:`jwt` authentication methods, KV v1 and v2 secret engines.
- It allows dynamic resolution of the Vault secret path using simple placeholders :literal:`{host}`\ , :literal:`{inventory\_hostname}` and :literal:`{user}`.
- The plugin caches Vault secrets in memory for a configurable duration to reduce load on the Vault server.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-control_path"></div>
      <p style="display: inline;"><strong>control_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-control_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>This is the location to save SSH&#x27;s ControlPath sockets, it uses SSH&#x27;s variable substitution.</p>
      <p>Since 2.3, if null (default), ansible will generate a unique hash. Use ``%(directory)s`` to indicate where to use the control dir path setting.</p>
      <p>Before 2.3 it defaulted to ``control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r``.</p>
      <p>Be aware that this setting is ignored if <code class='docutils literal notranslate'>-o ControlPath</code> is set in ssh args.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  control_path = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_CONTROL_PATH</code></p>

      </li>
      <li>
        <p>Variable: ansible_control_path</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-control_path_dir"></div>
      <p style="display: inline;"><strong>control_path_dir</strong></p>
      <a class="ansibleOptionLink" href="#parameter-control_path_dir" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>This sets the directory to use for ssh control path if the control path setting is null.</p>
      <p>Also, provides the ``%(directory)s`` variable for the control path setting.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;~/.ansible/cp&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  control_path_dir = ~/.ansible/cp</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_CONTROL_PATH_DIR</code></p>

      </li>
      <li>
        <p>Variable: ansible_control_path_dir</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-host"></div>
      <p style="display: inline;"><strong>host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Hostname/IP to connect to.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;inventory_hostname&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: inventory_hostname</p>

      </li>
      <li>
        <p>Variable: ansible_host</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_host</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-host_key_checking"></div>
      <p style="display: inline;"><strong>host_key_checking</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host_key_checking" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>Determines if SSH should reject or not a connection after checking host keys.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  host_key_checking = true</pre>

        <pre>[ssh_connection]
  host_key_checking = true</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.5</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HOST_KEY_CHECKING</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_HOST_KEY_CHECKING</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.5</i></p>

      </li>
      <li>
        <p>Variable: ansible_host_key_checking</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.5</i></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_host_key_checking</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.5</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Authentication password for the <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-remote_user"><span class="std std-ref"><span class="pre">remote_user</span></span></a></strong></code>. Can be supplied as CLI option.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_password</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_pass</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password_mechanism"></div>
      <p style="display: inline;"><strong>password_mechanism</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password_mechanism" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.19</i></p>

    </td>
    <td valign="top">
      <p>Mechanism to use for handling ssh password prompt</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;ssh_askpass&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;sshpass&#34;</code></p></li>
        <li><p><code>&#34;disable&#34;</code></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  password_mechanism = ssh_askpass</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_PASSWORD_MECHANISM</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_password_mechanism</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-pipelining"></div>
      <p style="display: inline;"><strong>pipelining</strong></p>
      <a class="ansibleOptionLink" href="#parameter-pipelining" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>Pipelining reduces the number of connection operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfers.</p>
      <p>This can result in a very significant performance improvement when enabled.</p>
      <p>However this can conflict with privilege escalation (<code class='docutils literal notranslate'>become</code>). For example, when using sudo operations you must first disable <code class='docutils literal notranslate'>requiretty</code> in the sudoers file for the target hosts, which is why this feature is disabled by default.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  pipelining = false</pre>

        <pre>[connection]
  pipelining = false</pre>

        <pre>[ssh_connection]
  pipelining = false</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_PIPELINING</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_PIPELINING</code></p>

      </li>
      <li>
        <p>Variable: ansible_pipelining</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_pipelining</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-pkcs11_provider"></div>
      <p style="display: inline;"><strong>pkcs11_provider</strong></p>
      <a class="ansibleOptionLink" href="#parameter-pkcs11_provider" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.12</i></p>

    </td>
    <td valign="top">
      <p>PKCS11 SmartCard provider such as opensc, example: /usr/local/lib/opensc-pkcs11.so</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  pkcs11_provider = &#34;&#34;</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_PKCS11_PROVIDER</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_pkcs11_provider</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td valign="top">
      <p>Remote port to connect to.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[defaults]
  remote_port = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_REMOTE_PORT</code></p>

      </li>
      <li>
        <p>Keyword: port</p>

      </li>
      <li>
        <p>Variable: ansible_port</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_port</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-private_key"></div>
      <p style="display: inline;"><strong>private_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-private_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.19</i></p>

    </td>
    <td valign="top">
      <p>Private key contents in PEM format. Requires the <code class='docutils literal notranslate'>SSH_AGENT</code> configuration to be enabled.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>ANSIBLE_PRIVATE_KEY</code></p>

      </li>
      <li>
        <p>Variable: ansible_private_key</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_private_key</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-private_key_file"></div>
      <p style="display: inline;"><strong>private_key_file</strong></p>
      <a class="ansibleOptionLink" href="#parameter-private_key_file" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to private key file to use for authentication.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[defaults]
  private_key_file = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_PRIVATE_KEY_FILE</code></p>

      </li>
      <li>
        <p>CLI argument: --private-key</p>

      </li>
      <li>
        <p>Variable: ansible_private_key_file</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_private_key_file</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-private_key_passphrase"></div>
      <p style="display: inline;"><strong>private_key_passphrase</strong></p>
      <a class="ansibleOptionLink" href="#parameter-private_key_passphrase" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.19</i></p>

    </td>
    <td valign="top">
      <p>Private key passphrase, dependent on <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-private_key"><span class="std std-ref"><span class="pre">private_key</span></span></a></strong></code>.</p>
      <p>This does NOT have any effect when used with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-private_key_file"><span class="std std-ref"><span class="pre">private_key_file</span></span></a></strong></code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>ANSIBLE_PRIVATE_KEY_PASSPHRASE</code></p>

      </li>
      <li>
        <p>Variable: ansible_private_key_passphrase</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_private_key_passphrase</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reconnection_retries"></div>
      <p style="display: inline;"><strong>reconnection_retries</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reconnection_retries" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td valign="top">
      <p>Number of attempts to connect.</p>
      <p>Ansible retries connections only if it gets an SSH error with a return code of 255.</p>
      <p>Any errors with return codes other than 255 indicate an issue with program execution.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[connection]
  retries = 0</pre>

        <pre>[ssh_connection]
  retries = 0</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_RETRIES</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_retries</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remote_user"></div>
      <p style="display: inline;"><strong>remote_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remote_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>User name with which to login to the remote server, normally set by the remote_user keyword.</p>
      <p>If no user is supplied, Ansible will let the SSH client binary choose the user as it normally.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[defaults]
  remote_user = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_REMOTE_USER</code></p>

      </li>
      <li>
        <p>CLI argument: --user</p>

      </li>
      <li>
        <p>Keyword: remote_user</p>

      </li>
      <li>
        <p>Variable: ansible_user</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_user</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-scp_executable"></div>
      <p style="display: inline;"><strong>scp_executable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-scp_executable" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.6</i></p>

    </td>
    <td valign="top">
      <p>This defines the location of the scp binary. It defaults to <code class="ansible-value literal notranslate">scp</code> which will use the first binary available in $PATH.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;scp&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  scp_executable = scp</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SCP_EXECUTABLE</code></p>

      </li>
      <li>
        <p>Variable: ansible_scp_executable</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-scp_extra_args"></div>
      <p style="display: inline;"><strong>scp_extra_args</strong></p>
      <a class="ansibleOptionLink" href="#parameter-scp_extra_args" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Extra exclusive to the <code class='docutils literal notranslate'>scp</code> CLI</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  scp_extra_args = &#34;&#34;</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SCP_EXTRA_ARGS</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>CLI argument: --scp-extra-args</p>

      </li>
      <li>
        <p>Variable: ansible_scp_extra_args</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-sftp_batch_mode"></div>
      <p style="display: inline;"><strong>sftp_batch_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sftp_batch_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>When set to <code class='docutils literal notranslate'>True</code>, sftp will be run in batch mode, allowing detection of transfer errors.</p>
      <p>When set to <code class='docutils literal notranslate'>False</code>, sftp will not be run in batch mode, preventing detection of transfer errors.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  sftp_batch_mode = true</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SFTP_BATCH_MODE</code></p>

      </li>
      <li>
        <p>Variable: ansible_sftp_batch_mode</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-sftp_executable"></div>
      <p style="display: inline;"><strong>sftp_executable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sftp_executable" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.6</i></p>

    </td>
    <td valign="top">
      <p>This defines the location of the sftp binary. It defaults to <code class="ansible-value literal notranslate">sftp</code> which will use the first binary available in $PATH.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;sftp&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  sftp_executable = sftp</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SFTP_EXECUTABLE</code></p>

      </li>
      <li>
        <p>Variable: ansible_sftp_executable</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-sftp_extra_args"></div>
      <p style="display: inline;"><strong>sftp_extra_args</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sftp_extra_args" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Extra exclusive to the <code class='docutils literal notranslate'>sftp</code> CLI</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  sftp_extra_args = &#34;&#34;</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SFTP_EXTRA_ARGS</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>CLI argument: --sftp-extra-args</p>

      </li>
      <li>
        <p>Variable: ansible_sftp_extra_args</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_args"></div>
      <p style="display: inline;"><strong>ssh_args</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_args" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Arguments to pass to all SSH CLI tools.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;-C -o ControlMaster=auto -o ControlPersist=60s&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  ssh_args = -C -o ControlMaster=auto -o ControlPersist=60s</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_ARGS</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_args</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_common_args"></div>
      <p style="display: inline;"><strong>ssh_common_args</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_common_args" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Common extra args for all SSH CLI tools.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  ssh_common_args = &#34;&#34;</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_COMMON_ARGS</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>CLI argument: --ssh-common-args</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_common_args</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_executable"></div>
      <p style="display: inline;"><strong>ssh_executable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_executable" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.2</i></p>

    </td>
    <td valign="top">
      <p>This defines the location of the SSH binary. It defaults to <code class="ansible-value literal notranslate">ssh</code> which will use the first SSH binary available in $PATH.</p>
      <p>This option is usually not required, it might be useful when access to system SSH is restricted, or when using SSH wrappers to connect to remote hosts.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;ssh&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  ssh_executable = ssh</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_EXECUTABLE</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_executable</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_extra_args"></div>
      <p style="display: inline;"><strong>ssh_extra_args</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_extra_args" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Extra exclusive to the SSH CLI.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  ssh_extra_args = &#34;&#34;</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_EXTRA_ARGS</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      <li>
        <p>CLI argument: --ssh-extra-args</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_extra_args</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_transfer_method"></div>
      <p style="display: inline;"><strong>ssh_transfer_method</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_transfer_method" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Preferred method to use when transferring files over ssh</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li>
          <p><code>&#34;piped&#34;</code>:
          Creates an SSH pipe with <code class='docutils literal notranslate'>dd</code> on either side to copy the data.</p>
        </li>
        <li>
          <p><code>&#34;scp&#34;</code>:
          Deprecated in OpenSSH. For OpenSSH &gt;=9.0 you must add an additional option to enable scp <code class='docutils literal notranslate'>scp_extra_args="-O"</code>.</p>
        </li>
        <li>
          <p><code>&#34;sftp&#34;</code>:
          This is the most reliable way to copy things with SSH.</p>
        </li>
        <li>
          <p><code style="color: blue;"><b>&#34;smart&#34;</b></code> <span style="color: blue;">(default)</span>:
          Tries each method in order (sftp &gt; scp &gt; piped), until one succeeds or they all fail.</p>
        </li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  transfer_method = smart</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_TRANSFER_METHOD</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_transfer_method</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.12</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-sshpass_prompt"></div>
      <p style="display: inline;"><strong>sshpass_prompt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sshpass_prompt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.10</i></p>

    </td>
    <td valign="top">
      <p>Password prompt that <code class='docutils literal notranslate'>sshpass</code>/<code class='docutils literal notranslate'>SSH_ASKPASS</code> should search for.</p>
      <p>Supported by sshpass 1.06 and up when <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-password_mechanism"><span class="std std-ref"><span class="pre">password_mechanism</span></span></a></strong></code> set to <code class="ansible-value literal notranslate">sshpass</code>.</p>
      <p>Defaults to <code class='docutils literal notranslate'>Enter PIN for</code> when pkcs11_provider is set.</p>
      <p>Defaults to <code class='docutils literal notranslate'>assword</code> when <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-password_mechanism"><span class="std std-ref"><span class="pre">password_mechanism</span></span></a></strong></code> set to <code class="ansible-value literal notranslate">ssh_askpass</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  sshpass_prompt = &#34;&#34;</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSHPASS_PROMPT</code></p>

      </li>
      <li>
        <p>Variable: ansible_sshpass_prompt</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td valign="top">
      <p>This is the default amount of time we will wait while establishing an SSH connection.</p>
      <p>It also controls how long we can wait to access reading the connection once established (select on the socket).</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">10</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  timeout = 10</pre>

        <pre>[ssh_connection]
  timeout = 10</pre>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.11</i></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_TIMEOUT</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_TIMEOUT</code></p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.11</i></p>

      </li>
      <li>
        <p>CLI argument: --timeout</p>

      </li>
      <li>
        <p>Variable: ansible_ssh_timeout</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.11</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-use_tty"></div>
      <p style="display: inline;"><strong>use_tty</strong></p>
      <a class="ansibleOptionLink" href="#parameter-use_tty" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.5</i></p>

    </td>
    <td valign="top">
      <p>add -tt to ssh commands to force tty allocation.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  usetty = true</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_USETTY</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_use_tty</p>
        <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.7</i></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_approle_mount_point"></div>
      <p style="display: inline;"><strong>vault_approle_mount_point</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_approle_mount_point" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Mount point of the AppRole auth backend.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;approle&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  approle_mount_point = approle</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_APPROLE_MOUNT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_approle_mount_point</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_auth_method"></div>
      <p style="display: inline;"><strong>vault_auth_method</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_auth_method" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Authentication method used against Vault.</p>
      <p><code class='docutils literal notranslate'>approle</code> uses <code class='docutils literal notranslate'>vault_role_id</code> / <code class='docutils literal notranslate'>vault_secret_id</code>.</p>
      <p><code class='docutils literal notranslate'>jwt</code> uses <code class='docutils literal notranslate'>vault_jwt</code> / <code class='docutils literal notranslate'>vault_jwt_path</code> with <code class='docutils literal notranslate'>vault_role</code>.</p>
      <p><code class='docutils literal notranslate'>token</code> uses <code class='docutils literal notranslate'>vault_token</code> directly.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;approle&#34;</code></p></li>
        <li><p><code>&#34;jwt&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;token&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  auth_method = token</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_AUTH_METHOD</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_auth_method</p>

      </li>
      <li>
        <p>Variable: vault_auth_method</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_ca_cert"></div>
      <p style="display: inline;"><strong>vault_ca_cert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_ca_cert" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to a CA bundle used to verify the Vault TLS certificate.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  ca_cert = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>VAULT_CACERT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_ca_cert</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_cache_ttl"></div>
      <p style="display: inline;"><strong>vault_cache_ttl</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_cache_ttl" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td valign="top">
      <p>Number of seconds a Vault secret is cached in memory (per worker process).</p>
      <p>Set to <code class='docutils literal notranslate'>0</code> to disable caching.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">300</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  cache_ttl = 300</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_cache_ttl</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_client_cert"></div>
      <p style="display: inline;"><strong>vault_client_cert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_client_cert" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to a client certificate for Vault mTLS.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_CLIENT_CERT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_client_cert</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_client_key"></div>
      <p style="display: inline;"><strong>vault_client_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_client_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to the client certificate key for Vault mTLS.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_CLIENT_KEY</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_client_key</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_enabled"></div>
      <p style="display: inline;"><strong>vault_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>Globally enable or disable the Vault credential lookup.</p>
      <p>When disabled the plugin behaves exactly like the standard <code class='docutils literal notranslate'>ssh</code> plugin.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  enabled = true</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_SSH_ENABLED</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_ssh_enabled</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_fail_on_missing"></div>
      <p style="display: inline;"><strong>vault_fail_on_missing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_fail_on_missing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>Fail the connection when the Vault secret cannot be retrieved.</p>
      <p>When <code class='docutils literal notranslate'>false</code>, the plugin logs a warning and falls back to standard SSH behaviour.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  fail_on_missing = true</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_fail_on_missing</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_jwt"></div>
      <p style="display: inline;"><strong>vault_jwt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_jwt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>The signed JWT/OIDC token used when <code class='docutils literal notranslate'>vault_auth_method=jwt</code>.</p>
      <p>If not provided, the plugin will try to read <code class='docutils literal notranslate'>vault_jwt_path</code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_JWT</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_JWT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_jwt</p>

      </li>
      <li>
        <p>Variable: vault_jwt</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_jwt_mount_point"></div>
      <p style="display: inline;"><strong>vault_jwt_mount_point</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_jwt_mount_point" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Mount point of the JWT/OIDC auth backend.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;jwt&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  jwt_mount_point = jwt</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_JWT_MOUNT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_jwt_mount_point</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_jwt_path"></div>
      <p style="display: inline;"><strong>vault_jwt_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_jwt_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to a file containing the JWT (e.g. Kubernetes service account token).</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;/var/run/secrets/kubernetes.io/serviceaccount/token&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  jwt_path = /var/run/secrets/kubernetes.io/serviceaccount/token</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_JWT_PATH</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_jwt_path</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_key_become_password"></div>
      <p style="display: inline;"><strong>vault_key_become_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_key_become_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Key inside the Vault secret holding the privilege escalation password.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;become_password&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  key_become_password = become_password</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_key_become_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_key_passphrase"></div>
      <p style="display: inline;"><strong>vault_key_passphrase</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_key_passphrase" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Key inside the Vault secret holding the private key passphrase.</p>
      <p>When set, the plugin uses <code class='docutils literal notranslate'>sshpass -P &#x27;Enter passphrase&#x27;</code> behaviour via ssh-agent free flow.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;private_key_passphrase&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  key_passphrase = private_key_passphrase</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_key_passphrase</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_key_password"></div>
      <p style="display: inline;"><strong>vault_key_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_key_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Key inside the Vault secret holding the SSH password.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;password&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  key_password = password</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_key_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_key_private_key"></div>
      <p style="display: inline;"><strong>vault_key_private_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_key_private_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Key inside the Vault secret holding the SSH private key (PEM content).</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;private_key&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  key_private_key = private_key</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_key_private_key</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_key_username"></div>
      <p style="display: inline;"><strong>vault_key_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_key_username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Key inside the Vault secret holding the SSH username.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;username&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  key_username = username</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_key_username</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_kv_version"></div>
      <p style="display: inline;"><strong>vault_kv_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_kv_version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Version of the KV secret engine.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;1&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;2&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  kv_version = 2</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_KV_VERSION</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_kv_version</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_mount_point"></div>
      <p style="display: inline;"><strong>vault_mount_point</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_mount_point" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Mount point of the KV secret engine.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;secret&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  mount_point = secret</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_MOUNT_POINT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_mount_point</p>

      </li>
      <li>
        <p>Variable: vault_mount_point</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_namespace"></div>
      <p style="display: inline;"><strong>vault_namespace</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_namespace" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Vault Enterprise namespace (e.g. <code class='docutils literal notranslate'>admin/team-a</code>).</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  namespace = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>VAULT_NAMESPACE</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HASHI_VAULT_NAMESPACE</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_namespace</p>

      </li>
      <li>
        <p>Variable: vault_namespace</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_prefer_static"></div>
      <p style="display: inline;"><strong>vault_prefer_static</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_prefer_static" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td valign="top">
      <p>When <code class='docutils literal notranslate'>true</code>, any credential already defined in the inventory / AAP credential takes precedence over the value retrieved from Vault.</p>
      <p>When <code class='docutils literal notranslate'>false</code> (default), Vault wins.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  prefer_static = false</pre>

      </li>
      <li>
        <p>Variable: ansible_vault_prefer_static</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_role"></div>
      <p style="display: inline;"><strong>vault_role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_role" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Vault role name to use with the JWT auth method.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_ROLE</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_ROLE</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_role</p>

      </li>
      <li>
        <p>Variable: vault_role</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_role_id"></div>
      <p style="display: inline;"><strong>vault_role_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_role_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>AppRole RoleID used when <code class='docutils literal notranslate'>vault_auth_method=approle</code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_ROLE_ID</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HASHI_VAULT_ROLE_ID</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_role_id</p>

      </li>
      <li>
        <p>Variable: vault_role_id</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_secret_id"></div>
      <p style="display: inline;"><strong>vault_secret_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_secret_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>AppRole SecretID used when <code class='docutils literal notranslate'>vault_auth_method=approle</code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_SECRET_ID</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HASHI_VAULT_SECRET_ID</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_secret_id</p>

      </li>
      <li>
        <p>Variable: vault_secret_id</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_secret_path"></div>
      <p style="display: inline;"><strong>vault_secret_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_secret_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td valign="top">
      <p>Path of the secret inside the KV engine, relative to the mount point.</p>
      <p>Supports Jinja-free simple placeholders <code class='docutils literal notranslate'>{host}</code>, <code class='docutils literal notranslate'>{inventory_hostname}</code> and <code class='docutils literal notranslate'>{user}</code>.</p>
      <p>Example <code class='docutils literal notranslate'>hosts/{host}</code> or <code class='docutils literal notranslate'>linux/{inventory_hostname}</code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  secret_path = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_SECRET_PATH</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_secret_path</p>

      </li>
      <li>
        <p>Variable: vault_secret_path</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_timeout"></div>
      <p style="display: inline;"><strong>vault_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td valign="top">
      <p>Timeout (seconds) for HTTP requests to Vault.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">30</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  timeout = 30</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_TIMEOUT</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_timeout</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_token"></div>
      <p style="display: inline;"><strong>vault_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_token" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Vault token used when <code class='docutils literal notranslate'>vault_auth_method=token</code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VAULT_TOKEN</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HASHI_VAULT_TOKEN</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_token</p>

      </li>
      <li>
        <p>Variable: vault_token</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_token_file"></div>
      <p style="display: inline;"><strong>vault_token_file</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_token_file" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Path to a file containing a Vault token (e.g. <code class='docutils literal notranslate'>~/.vault-token</code>).</p>
      <p>Used as a fallback when <code class='docutils literal notranslate'>vault_token</code> is not set.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;~/.vault-token&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  token_file = ~/.vault-token</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_TOKEN_FILE</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_token_file</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_url"></div>
      <p style="display: inline;"><strong>vault_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td valign="top">
      <p>URL of the HashiCorp Vault server (e.g. <code class='docutils literal notranslate'>https://vault.example.com:8200</code>).</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  url = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>VAULT_ADDR</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_HASHI_VAULT_ADDR</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_url</p>

      </li>
      <li>
        <p>Variable: vault_url</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vault_verify"></div>
      <p style="display: inline;"><strong>vault_verify</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vault_verify" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Whether to verify the Vault server TLS certificate.</p>
      <p>Can also be a path to a CA bundle.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;true&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[vault_ssh_connection]
  verify = true</pre>

      </li>
      <li>
        <p>Environment variable: <code>VAULT_SKIP_VERIFY_INVERTED</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_VAULT_VERIFY</code></p>

      </li>
      <li>
        <p>Variable: ansible_vault_verify</p>

      </li>
      <li>
        <p>Variable: vault_verify</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-verbosity"></div>
      <p style="display: inline;"><strong>verbosity</strong></p>
      <a class="ansibleOptionLink" href="#parameter-verbosity" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible.posix 2.19</i></p>

    </td>
    <td valign="top">
      <p>Requested verbosity level for the SSH CLI.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[ssh_connection]
  verbosity = 0</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_SSH_VERBOSITY</code></p>

      </li>
      <li>
        <p>Variable: ansible_ssh_verbosity</p>

      </li>
      </ul>
    </td>
  </tr>
  </tbody>
  </table>



.. note::

    Configuration entries listed above for each entry type (Ansible variable, environment variable, and so on) have a low to high priority order.
    For example, a variable that is lower in the list will override a variable that is higher up.
    The entry types are also ordered by precedence from low to high priority order.
    For example, an ansible.cfg entry (further up in the list) is overwritten by an Ansible variable (further down in the list).


Notes
-----

- This plugin is mostly a wrapper to the \`\`ssh\`\` CLI utility and the exact behavior of the options depends on this tool. This means that the documentation provided here is subject to be overridden by the CLI tool itself.
- Many options default to :literal:`None` here but that only means we do not override the SSH tool's defaults and/or configuration. For example, if you specify the port in this plugin it will override any :literal:`Port` entry in your :literal:`.ssh/config`.
- The ssh CLI tool uses return code 255 as a 'connection error', this can conflict with commands/tools that also return 255 as an error code and will look like an 'unreachable' condition or 'connection error' to this plugin.


Examples
--------

.. code-block:: yaml

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






Authors
~~~~~~~

- Clément Perrin (@cleymax)


Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/Cleymax/ansible\_global\_collection/issues>`__
* `Repository (Sources) <https://github.com/Cleymax/ansible\_global\_collection>`__
