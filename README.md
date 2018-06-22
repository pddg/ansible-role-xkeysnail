ansible-role-xkeysnail
======================

To install xkeysnail and register autostart handled by GNOME.

Requirements
------------

You must be able to use `sudo`.  
And python3 is required. xkeysnail will be installed by `pip` (`python3-pip`).

Role Variables
--------------

- `xkeysnail_config_dir`
  - To store configulation files
  - Default is `/etc/opt/xkeysnail`
  - Must be readable by other user (do not specify `~/.config/xxxx`)
- `xkeysnail_config_file`
  - Specify configulation file written with python
  - Default is `config.py` in `files` dir.
  - Do **not** contain `/` at the end of path.

Dependencies
------------

No other requirements.

Example Playbook
----------------

This role is supposed to be used locally. Keep in mind that the name of the executing user is written to `/etc/sudoers.d/10-install`.

```yaml
- hosts: localhost
  roles:
    - name: pddg.ansible-role-xkeysnail
      vars:
        xkeysnail_config_dir: /etc/opt/xkeysnail
        xkeysnail_config_file: /path/to/config.py
```

You should use `-K` option when use playbook. This role require `sudo`.

```bash
$ ansible-playbook hoge.yml -K
```

License
-------

MIT

Author Information
------------------

- Author: pddg
- Web: https://www.poyo.info
- Org: [Studio Aquatan](https://www.aquatan.studio/)

