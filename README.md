# Godaddy API

## Clone
```
git clone https://github.com/tuyendq/godaddyapi.git
cd godaddyapi
```
## Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Environment variables
### Create .env file at root folder
```
# OTE https://api.ote-godaddy.com
# GODADDY_API_KEY=your-ote-key
# GODADDY_API_SECRET=your-ote-secret
# URL_API='https://api.ote-godaddy.com'

# Produciton https://api.godaddy.com
GODADDY_API_KEY=your-production-key
GODADDY_API_SECRET=your-production-secret
API_URL='https://api.godaddy.com'
```

### Install required packages
```
pip install -r requirements.txt
```
