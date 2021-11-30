# SelfStorage

![SelfStorage site](/static/img/selfstorage.png)

## Description

The app represents an MVP of storage ordering web-app. It has 3 tabs:

- index tab with a map and the description of all storages
- tab responsible for storage box rent
- tab responsible for seasonal items deposit

Both second and third tabs allow imitating user order process.

In the first case, the user can choose a warehouse, the size of the box, and the rental duration.
In the second case, the user can choose a warehouse, an item to deposit, its quantity, and deposit duration.
Also, the user has the possibility to apply a promo code if he possesses one.

After submitting an order, the user is redirected to an application form where he's asked to fill his personal info in.
After he's redirected to a dummy payment page.
After successful payment, the user receives on his email a QR-code with access to the ordered box.

## Install

At least Python3.8, Git and Poetry should be already installed.

For production, Docker is also required.

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

#### Development version

3. Rename `.env.example` to `.env` and change `SECRET_KEY` environment variable

- `SECRET_KEY`  - django secret key

4. Create superuser

```
python manage.py createsuperuser
```

5. Migrate the database

```
python manage.py migrate
```


#### Production version

3. Rename `.env.dev.example` to `.env.dev` and change environment variables (at least `SECRET_KEY`)

- `SECRET_KEY`  - djngo secret key
- `POSTGRES_DB` - name of the database
- `POSTGRES_USER` - username for the database
- `POSTGRES_PASSWORD` - password for the database

## Run

#### Development version

```
python manage.py runserver
```

Site will be available via `127.0.0.1:8000`

#### Production version

```
docker compose up --build
```

Site will be available via `127.0.0.1`
