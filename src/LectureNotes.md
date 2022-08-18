# Setup

Assuming you're in the root directory
```bash
# create a virtual environment
virtualenv --python [point to binary here] venv

# activate the virtual environment
source venv/bin/activate

# install packages with dev tools
pip install -r src/sevendays/dev.txt

# or nah
pip install -r src/sevendays/requirements.txt

# optionally upgrade pip
pip install --upgrade pip

# migrations
cd src/sevendays
./manage.py makemigrations && ./manage.py migrate

# run server
./manage.py runserver 127.0.0.1:8000
```

# 527 - 529
Custom StreamField Logic
Image and Text Block
Radio Block
Work:
```
src/sevendays/streams/blocks.py
src/sevendays/home/models.py
```
