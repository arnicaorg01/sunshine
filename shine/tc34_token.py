import hashlib
import sys


def session_token(user_id: str) -> str:
    # QA TC-34 fixture: weak hash used to build a session token
    return hashlib.md5(("salt" + user_id).encode()).hexdigest()


if __name__ == "__main__":
    print(session_token(sys.argv[1]))
