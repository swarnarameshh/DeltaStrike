# DeltaStrike 

AI-Powered Options Signal Generation Platform for NSE & BSE Indices

## Overview

DeltaStrike is a real-time options monitoring and signal generation platform designed for Indian stock market indices.

The application connects to AccelPix market data APIs, streams live option chain data, evaluates custom trading strategies based on Delta and Premium conditions, and sends instant Telegram alerts when trading opportunities are detected.

## Supported Indices

### NSE

- NIFTY
- BANKNIFTY
- FINNIFTY
- MIDCAPNIFTY

### BSE

- SENSEX
- BANKEX

---

## Strategy Logic

The strategy focuses on identifying low-premium option contracts near expiry and capturing rapid premium movement.

### Entry Conditions

- Monitor ATM strikes and nearby strikes
- NSE:
  - ATM + 5 strikes above
  - ATM + 5 strikes below
  - Total: 11 strikes
- BSE:
  - ATM + 10 strikes above
  - ATM + 10 strikes below
  - Total: 21 strikes

### Delta Filter

```text
0.50 <= Delta <= 0.58
```

### Premium Filter

```text
Premium approximately ₹30 - ₹50
```

### Signal Selection

- Closest ATM strike
- ATM ITM CE
- ATM ITM PE

### Stop Loss

```text
Stop Loss = Premium - (Premium × 40%)
```

Example:

```text
Premium = 50

SL = 50 - (50 × 0.40)

SL = 30
```

---

## Telegram Alerts

When conditions are satisfied, DeltaStrike generates a Telegram notification containing:

- Index
- Strike Price
- Buy Price
- Stop Loss

Example:

```text
🚨 DeltaStrike Alert

Index      : NIFTY
Strike     : 24900 CE
Buy Price  : 50
Stop Loss  : 30
```

---

## Project Structure

```text
DeltaStrike/
│
├── app/
│   ├── config/
│   ├── dashboard/
│   ├── models/
│   ├── services/
│   ├── strategy/
│   └── telegram/
│
├── tests/
│
├── .env
├── requirements.txt
├── README.md
└── main.py
```

---

## Technology Stack

- Python 3.13
- AccelPix Market Data API
- AsyncIO
- Telegram Bot API
- Git & GitHub

Future Enhancements:

- Streamlit Dashboard
- Historical Signal Analytics
- Trade Journal
- Strategy Backtesting
- Cloud Deployment

---

## Installation

### Clone Repository

```bash
git clone https://github.com/swarnarameshh/DeltaStrike.git
cd DeltaStrike
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
ACCELPIX_API_KEY=your_api_key
ACCELPIX_HOST=apidata.accelpix.in

TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## Current Development Status

### Phase 1

- [x] Project Setup
- [x] GitHub Repository
- [x] AccelPix Connection
- [x] ATM Calculator

### Phase 2

- [ ] Live Spot Price Listener
- [ ] Strike Generator
- [ ] Option Chain Subscription

### Phase 3

- [ ] Greeks Engine
- [ ] Delta Filter
- [ ] Signal Engine

### Phase 4

- [ ] Telegram Notifications

### Phase 5

- [ ] Dashboard

---

## Author

Swarna Ramesh


---

## Disclaimer

This project is for educational and research purposes only.

Trading in financial markets involves risk. Users are solely responsible for their trading decisions.
