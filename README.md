# Wealth Management Portfolio Tracker

A comprehensive Flask-based web application for personal investment portfolio management, featuring real-time market data, AI-powered investment strategies, and performance analytics.

## 🚀 Features

### Core Functionality
- **User Authentication & Profiles**: Secure login/registration with user profiles
- **Portfolio Management**: Track stocks, cryptocurrencies, and mutual funds
- **Real-time Market Data**: Live price updates using Alpha Vantage API and yfinance
- **Performance Analytics**: Comprehensive portfolio performance tracking and visualization
- **Investment Strategies**: AI-powered investment recommendations and strategy optimization
- **Risk Management**: Risk tolerance assessment and portfolio diversification

### Technical Features
- **Flask Web Framework**: Modern Python web application
- **PostgreSQL Database**: Robust data storage with SQLAlchemy ORM
- **Database Migrations**: Alembic for schema management
- **Responsive UI**: Clean, modern interface with Bootstrap styling
- **RESTful APIs**: JSON endpoints for market data and portfolio operations

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL database
- Alpha Vantage API key (for market data)
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flaskProject4
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://username:password@localhost/database_name
   ALPHA_VANTAGE_API_KEY=your-alpha-vantage-api-key
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## 🏗️ Project Structure

```
flaskProject4/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── extensions.py         # Flask extensions initialization
├── requirements.txt      # Python dependencies
├── migrations/           # Database migration files
├── static/              # Static assets (CSS, JS, images)
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── dashboard.html   # Main dashboard
│   ├── portfolio.html   # Portfolio management
│   └── ...
├── users/               # User management module
│   ├── models.py        # User model
│   ├── routes.py        # Authentication routes
│   └── utils.py         # User utilities
├── portfolio/           # Portfolio management module
│   ├── models.py        # Asset models (stocks, crypto, funds)
│   ├── routes.py        # Portfolio routes
│   └── utils.py         # Portfolio utilities
├── market_data/         # Market data module
│   ├── routes.py        # Market data API routes
│   ├── utils.py         # Market data utilities
│   └── alpha_vantage_config.py  # API configuration
├── strategies/          # Investment strategies module
│   ├── models.py        # Strategy models
│   ├── routes.py        # Strategy routes
│   ├── ai_model.py      # AI recommendation engine
│   ├── optimizer.py     # Portfolio optimization
│   └── utils.py         # Strategy utilities
├── performance/         # Performance analytics module
│   ├── routes.py        # Performance routes
│   └── utils.py         # Analytics utilities
└── overview/            # Overview dashboard module
    └── routes.py        # Overview routes
```

## 🗄️ Database Models

### User Management
- **User**: User accounts with authentication, risk tolerance, and investment goals

### Portfolio Assets
- **StockHolding**: Individual stock investments
- **CryptoHolding**: Cryptocurrency investments
- **MutualFundHolding**: Mutual fund investments

### Investment Strategies
- **InvestmentStrategy**: User-defined investment strategies with risk profiles and allocations

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for session management
- `DATABASE_URL`: PostgreSQL connection string
- `ALPHA_VANTAGE_API_KEY`: API key for Alpha Vantage market data

### Database Configuration
The application uses PostgreSQL with the following default configuration:
- Host: localhost
- Database: wm_db
- Username: wm
- Password: password

## 📊 API Endpoints

### Market Data
- `GET /stock?symbol=AAPL` - Get stock price data
- `GET /crypto?symbol=BTC&market=USD` - Get cryptocurrency price data
- `GET /fund?symbol=VTSAX` - Get mutual fund price data

### Portfolio Management
- `GET /portfolio` - View user portfolio
- `POST /portfolio/add_stock` - Add stock to portfolio
- `POST /portfolio/add_crypto` - Add cryptocurrency to portfolio
- `POST /portfolio/add_fund` - Add mutual fund to portfolio

### User Management
- `GET /login` - User login page
- `POST /register` - User registration
- `GET /profile` - User profile management

## 🎯 Key Features Explained

### Portfolio Tracking
- Add and manage multiple asset types (stocks, crypto, mutual funds)
- Track purchase prices, quantities, and current market values
- Real-time portfolio valuation and performance metrics

### Market Data Integration
- Real-time stock prices via Alpha Vantage API
- Cryptocurrency data via yfinance
- Mutual fund information and pricing

### Investment Strategies
- AI-powered investment recommendations
- Portfolio optimization algorithms
- Risk-adjusted return analysis
- Diversification suggestions

### Performance Analytics
- Portfolio performance tracking over time
- Asset allocation visualization
- Risk metrics and analysis
- Comparative performance benchmarks

## 🔒 Security Features

- Password hashing with Werkzeug
- Flask-Login for session management
- CSRF protection
- Secure database connections
- Environment variable configuration

## 🔄 Version History

- **v1.0.0**: Initial release with basic portfolio management
- **v1.1.0**: Added market data integration
- **v1.2.0**: Implemented AI investment strategies
- **v1.3.0**: Enhanced performance analytics

## 📞 Contact

- Project Link: (https://github.com/pra-nali1812/flaskProject4)
- Email:bhusalpranali2016@gmail.com

---

**Note**: This application is for educational and personal use. Always consult with financial advisors before making investment decisions. 
