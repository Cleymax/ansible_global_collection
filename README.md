# Ansible Collection - cleymax.ansible_global_collection

The Ansible Collection for several global roles and modules, which can be used in any Ansible playbook.


## Requirements

- **Ansible-Core**: >= 2.18.0
- **Python**: With ansible-core, as listed for control nodes [here](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix)
- No additional Python libraries or external Ansible collections are required.

## Installation

Install the collection from Ansible Galaxy using:

```bash
ansible-galaxy collection install cleymax.ansible_global_collection
```

Or include it in a `requirements.yml` file:

```yaml
collections:
  - name: cleymax.ansible_global_collection
```

To upgrade the collection to the latest version:

```bash
ansible-galaxy collection install cleymax.ansible_global_collection --upgrade
```

To install a specific version:

```bash
ansible-galaxy collection install cleymax.ansible_global_collection:==1.0.0
```

See the full guide on [using Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more.

## Use Cases

### Connection Plugins

| Name | Description |
|------|-------------|
| vault_ssh | A connection plugin that retrieves SSH credentials from HashiCorp Vault and establishes an SSH connection to the target host. |


## Related Information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)

## License Information

This collection is licensed under the GNU General Public License v3.0 or later.
See: [https://www.gnu.org/licenses/gpl-3.0.txt](https://www.gnu.org/licenses/gpl-3.0.txt)

