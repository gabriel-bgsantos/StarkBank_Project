import starkbank

def authenticator():
    private_key_content = "insert your private key here"

    project = starkbank.Project(
        environment = "sandbox",
        id = "your project id",
        private_key = private_key_content
    )

    starkbank.user = project
    balance = starkbank.balance.get(user=project)
    starkbank.language = "en-US"