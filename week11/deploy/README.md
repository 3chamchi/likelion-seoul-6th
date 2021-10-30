장고 배포
---

# EC2 초기 설정

```shell
sudo apt-get update
sudo apt-get upgrade -y

# Install Pyenv Dependencies
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

# Install Pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\nfi' >> ~/.bashrc


# Install Pyenv Dependencies
sudo apt-get install -y gcc g++ build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Install Python 3.10 with Pyenv
pyenv install 3.9.7
pyenv global 3.9.7

# Install Gunicorn
python -m pip install gunicorn

gunicorn config.wsgi:application --bind 0:8000
```

```
# Install Nginx
sudo apt-get install -y nginx
```