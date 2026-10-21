<div align="center">

<img src="https://gitlab.com/progineous/progineous/-/raw/main/logo.png" alt="Pro Gineous" width="280">

</div>

Pro Gineous sells domains, shared hosting, VPS and dedicated servers. This account is where the scripts and server configs are published.

[Website](https://progineous.com) · [Blog](https://blog.progineous.com) · [X](https://x.com/ProGineous) · [LinkedIn](https://www.linkedin.com/company/progineous/) · [Instagram](https://www.instagram.com/progineous/)

## Scripts

| Repo | What it does |
| --- | --- |
| [who-is-eating-my-server](https://github.com/progineousgb/who-is-eating-my-server) | Two-second sample of CPU, RAM, disk and network, named by process, service or container. Read-only. |
| [vps-audit](https://github.com/progineousgb/vps-audit) | Scores a Linux VPS on basic security checks and prints the fix for each finding. Does not change the server. |
| [ssl-watch](https://github.com/progineousgb/ssl-watch) | Certificate expiry for domains configured on the server. Warns under 14 days, critical under 7. For cron. |
| [docker-cleanup-report](https://github.com/progineousgb/docker-cleanup-report) | Docker disk use, split into safe and risky cleanup, with the commands to run. Deletes nothing. |
| [server-toolkit](https://github.com/progineousgb/server-toolkit) | Bash scripts for VPS hardening, disk usage, RDAP domain expiry, DNS, DMARC and WordPress backups. Read-only unless a flag says otherwise. |

## Configs and notes

- [nginx-configs](https://github.com/progineousgb/nginx-configs): server blocks for a static site, WordPress, Laravel and a reverse proxy, plus TLS and rate-limit snippets. Debian and Ubuntu paths.
- [compose-stacks](https://github.com/progineousgb/compose-stacks): Compose projects for WordPress, Nextcloud, Vaultwarden, n8n, Umami and Uptime Kuma. Each app is its own project, behind one Caddy proxy.
- [vps-bootstrap](https://github.com/progineousgb/vps-bootstrap): cloud-init and Ansible for a new Debian or Ubuntu VPS. SSH keys only, UFW, fail2ban, unattended upgrades.
- [gitlab-ci-templates](https://github.com/progineousgb/gitlab-ci-templates): GitLab CI jobs that deploy to a Linux server over SSH. Static sites, Compose, Laravel releases, or one WordPress theme or plugin.
- [dns-email-records](https://github.com/progineousgb/dns-email-records): example MX, SPF, DKIM, DMARC and MTA-STS records for Google Workspace, Microsoft 365, Zoho and a self-hosted mail server.
- [awesome-self-hosting-vps](https://github.com/progineousgb/awesome-self-hosting-vps): apps that fit on one small VPS (about 1 to 4 GB of RAM), linked to each project's own site.

## From the blog

- [Disk full on a Linux VPS](https://blog.progineous.com/vps-disk-full/)
- [Secure a Linux VPS in 15 minutes](https://blog.progineous.com/secure-linux-vps-15-minutes/)
- [Check a domain's expiry with RDAP](https://blog.progineous.com/rdap-domain-lookup/)

dev@progineous.com · London
