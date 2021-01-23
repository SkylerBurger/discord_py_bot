# Discord Py Bot Template

This repo is a template for building a Discord bot using the [**discord.py**](https://github.com/Rapptz/discord.py) package.

This template is structured to use and test bot cogs built with discord.py's [**Bot Commands Framework**](https://discordpy.readthedocs.io/en/latest/ext/commands/index.html). This template also has GitHub Actions enabled for Continuous Integration, verifying your bot code with `pytest` and `flake8` on Python versions 3.8 and 3.9 upon pushes and merges to `main`. Edit `.github/workflows/tests.yml` to customize this behavior.

## Getting Started

1. Generate a new repository based off of this template repository.

2. Clone the repository to your machine, create a virtual environment for your bot, and install the required dependencies.
    - This project requires Python 3.8+ to utilize the AsyncMock object in testing.
    - This template has required dependecies listed in a standard `requirements.txt` file and additionally in a `pyproject.toml` file for those that use [`poetry`]
    (https://python-poetry.org/) for dependency management.
3. Create an Application on [Discord's Developer Portal](https://discord.com/developers/applications). Go to the 'Bot' settings for your application and click *Add Bot*. Then click *Reveal Token* and copy the token string.

4. Create a `.env` file at the root level of the repository and paste the token for your bot into the file as *BOT_TOKEN*.
    ```bash
    # Example .env
    BOT_TOKEN=asd151v38rsdsv136asd5f1v35sadgf1
    ```

5. Create an OAuth2 URL to invite your bot to a Discord server by going to the *OAuth2* settings for your application and selecting the 'bot' checkbox under 'scopes'. Select the permissions you wish to give your bot under 'bot permissions'. Once all of the required permissions have been selected you can copy the OAuth2 URL at the bottom of the 'scopes' section.
    - Permissions required for your bots will vary. A good starting selection will include: 'view channels', 'send messages', 'manage messages', 'embed links', 'attach files', 'read message history', 'mention everyone', 'use external emojis', and 'add reactions'.

6. Enter the OAuth2 URL into your browser and invite your bot to a Discord server you control.
    - Note, you can repeat steps 5 and 6 to invite your bot to multiple servers during and after development. Send the link to another person if you'd like to allow them to invite the bot to a server they control.

5. Develop functionality for your bot in cog files located in `cogs/` and write tests for your cogs within `tests/`.
    - This template was built with `pytest` and `flake8` in mind for testing and linting. Run `pytest` in the terminal to execute your test files and `flake8 .` to run a Python linting check over the repository.
