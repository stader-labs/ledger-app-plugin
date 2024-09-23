# Ledger Staderlabs Plugin

This is a plugin for the Ethereum application which helps parsing and displaying relevant information when signing a Staderlabs transaction.

## Setup

1. Clone this repo (along with git submodules)
    ```shell
    git clone --recurse-submodules https://github.com/LedgerHQ/app-plugin-staderlabs.git
    ```

2. Make sure you have an X11 server running:
    - On Ubuntu Linux, it should be running by default
    - On macOS, install and launch XQuartz (make sure to go to XQuartz > Preferences > Security and check "Allow client connections")
    - On Windows, install and launch VcXsrv (make sure to configure it to disable access control)

3. Install and run docker desktop

4. Install the [Ledger Dev Tools VS Code plugin](https://marketplace.visualstudio.com/items?itemName=LedgerHQ.ledger-dev-tools&ssr=false#overview) and makes sure it's enabled

5. Once you have installed the plugin and open the repo, the plugin should by default try to create and start the containers. If it doesn't, you can simply click "Update Container" under "Ledger Dev Tools" in the Activity Side Bar on VS Code.

6. On the "Ledger Dev Tools" side bar, Select a target and then click on Build.

7. Once build is complete, click on "Run tests" to run the tests


## Smart Contracts

Smart contracts covered by this plugin are documented in [PLUGIN_SPECIFICATON.md](https://github.com/LedgerHQ/app-plugin-staderlabs/blob/develop/PLUGIN_SPECIFICATION.md)
