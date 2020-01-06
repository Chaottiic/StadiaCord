# Stadiacord
[![GitHub Release](https://img.shields.io/github/v/release/Chaottiic/Stadiacord.svg?include_prereleases)]() [![GitHub Download Count](https://img.shields.io/github/downloads/Chaottiic/Stadiacord/total.svg)]() [![GitHub Issues Open](https://img.shields.io/github/issues/Chaottiic/Stadiacord/total.svg)]()

> NOTICE: WE ARE NOT DONE WITH THE WINDOWS CLIENT 

This integration sets a Discord Rich Presence of your current Stadia Game

# MacOS

- Extract files from build.zip
- Configure settings.json
```JSON
{
    "settings": {
        "IGN": "Splash",
        "WEBSITE": "stadia.com",
        "DEBUG": "True"
    }
}
```

- Run main.exec
- "Terminal" wants access to control "Google Chrome" -> Ok
- Go to Discord -> Settings -> Game Activity -> Enabled
> If this does not work, please go below and compile it. Some modules may be missing and need to be compiled freshly.

## Compiling
> Not required unless you want to edit source code.
- Go into Terminal
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements-mac.txt
python3 setup.py build
```
- Go into build/ and run main
- "Terminal" wants access to control "Google Chrome" -> Ok
- Go to Discord -> Settings -> Game Activity -> Enabled

# Windows
>Coming Soon.

[GitHub Release]: https://github.com/Chaottiic/StadiaCord/releases
[GitHub Download Count]: https://github.com/Chaottiic/StadiaCord/releases
[GitHub Issues Open]: https://github.com/Chaottiic/StadiaCord/issues