# Ansible Playbook: Linux Configuration and Nginx Deployment

This Ansible playbook automates the configuration of a Linux machine and deploys an Nginx server with custom virtual host configurations.

## Features

- User management (creation and SSH key setup)
- System configuration (timezone, MOTD, NTP)
- Root password change
- Nginx installation and configuration

## Prerequisites

- Ansible 2.9 or higher
- Target Linux machines accessible via SSH

## Structure

```
.
├── playbook.yaml
├── vars
│   └── main.yaml
└── templates
    ├── motd
    ├── ntp.conf
    └── example.com.conf
    └── test.com.conf
```

## Usage

1. Clone this repository or copy the files to your Ansible control node.

2. Modify the `vars/main.yaml` file to set your desired values:
   - User information (usernames, passwords, SSH public keys)
   - Timezone
   - Root password
   - Nginx virtual host configurations

3. Update your Ansible inventory file with the target hosts.

4. Run the playbook:

   ```
   ansible-playbook -i inventory playbook.yaml
   ```

## Playbook Tasks

1. Add new users
2. Add SSH public keys for new users
3. Set timezone
4. Set custom message of the day (MOTD)
5. Install and configure NTP
6. Change root password
7. Install Nginx
8. Configure and enable Nginx virtual hosts
