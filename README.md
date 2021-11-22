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
