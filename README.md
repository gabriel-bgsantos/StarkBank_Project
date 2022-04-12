# StarkBank-test
Start with the main.py =)

# The Test
1. Issues 8 to 12 Invoices every 3 hours to random people for 24 hours (our Sandbox
emulation environment will make sure some of those are automatically paid);

2. Receives the webhook callback of the Invoice credit and sends the received amount
(minus eventual fees) to an account from the Sandbox using a Transfer

# The Steps
Before running it you're gonna need these two little packages from pip
```
sudo pip install names
```
```
sudo pip install cpf-generator
```
