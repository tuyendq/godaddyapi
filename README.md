# Godaddy API

## Usage
Create or update IP Address of an A DNS record on Godaddy
```bash
python3 godaddyapi.py 'domain_name' 'record_name'
```

## Clone
```bash
git clone https://github.com/tuyendq/godaddyapi.git
cd godaddyapi
```
## Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Environment variables
### Create .env file at root folder
```bash
# OTE https://api.ote-godaddy.com
# GODADDY_API_KEY=your-ote-key
# GODADDY_API_SECRET=your-ote-secret
# URL_API_BASE='https://api.ote-godaddy.com'

# Production https://api.godaddy.com
GODADDY_API_KEY=your-production-key
GODADDY_API_SECRET=your-production-secret
API_URL_BASE='https://api.godaddy.com'
```

### Install required packages
```
pip install -r requirements.txt
```
