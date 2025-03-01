# Necker Fintech Payment Platform

Necker Fintech Payment Platform is a **multi-currency payment gateway** supporting **cryptocurrency (Kraken)** and **traditional payment methods (Alipay, WeChat Pay)**. The platform allows users to scan a QR code to complete payments seamlessly.

## 🚀 Features
- **Multi-Payment Support**: Kraken (crypto), Alipay, WeChat Pay.
- **QR Code Payments**: Auto-generated wallet address & amount.
- **Real-time Payment Status**: Webhook integration for auto-confirmation.
- **Lightweight & Scalable**: Built with FastAPI (Python) & Next.js (React).

## 📌 Tech Stack
- **Backend**: FastAPI (Python), PostgreSQL/SQLite, Webhooks
- **Frontend**: Next.js (React)
- **Deployment**: AWS / Vercel / DigitalOcean

## 📖 Getting Started
1. Clone the repo: `git clone https://github.com/kaiyanzzz/necker-fintech-payment-platform.git`
2. Install dependencies: `pip install -r requirements.txt && npm install`
3. Start backend: `uvicorn app:app --reload`
4. Start frontend: `npm run dev`
5. Open `http://localhost:3000` to test payments!

## 🌟 Future Enhancements
- **Auto-withdrawal system**
- **Binance Pay, PayPal, Stripe support**
- **Admin dashboard for merchants**
