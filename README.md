# PacktPubExplorer

![Status:Active](https://img.shields.io/badge/Project_Status-Active-brightgreen.svg)

Small script, meant to be run at boot, that by default creates a .packt file containing today's Free Learning Ebook's title. The file can be used in Conky for Displaying on your desktop via the "cat" command

Helpful arguments:

- `--conky`: Does some small escaping to avoid possible issues in Conky Configurations;
- `--notify`: Uses Notify-Send to send a notification instead of creating a `~/.packt` File;
- `--api`: Uses the api-based scraping approach (legacy);
