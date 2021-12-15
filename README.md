# PisonMLChallenge1-zShaffer

## Installation
Download the package from GitHub and extract to a local directory. The setuptools for uploading for PIP installation weren't working with Python 3.8 and I have not been able to fix it yet.

## Developer Notes
Unfortunately I was not able to get this working to the full functionality expected. I am able to scan for local Bluetooth GATT connections and send them to the website but the formatting does not work too well. Instead of replacing the values at every x seconds it just continues to write to the list of connections. Following this the scan refresh is currently set at a fixed interval of 5 seconds instead of taking in the user input. However the server uptime displays correctly! Thank you for these challenges, they were very informative and I have learned a lot in the past week!
