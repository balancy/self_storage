# SelfStorage

## Install

At least Python3.8, Git and Poetry should be already installed.

1. Clone the repository
```
git clone git@github.com:balancy/self_storage.git
```

2. Go inside cloned repo, install depenencies and activate virtual environment
```
cd self_storage
poetry install
poetry shell
```

3. Rename `.env.example` to `.env` and define environment variables

- `SECRET_KEY`  - django secret key
- `DEBUG`       - if True, django is in dev mode
