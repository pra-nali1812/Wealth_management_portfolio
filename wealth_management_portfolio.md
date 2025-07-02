
 Wealth Management Portfolio
Project Name:Wealth Management Portfolio  
Module
  1.Users
  2.Portfolio
  3.Market Data
  4.Strategies
  5.Performance
Developed By:Pranali  
Start Date: 2 April 2025  
Project Status: Hold 
Description
The Wealth Management Portfolio Tracker allows users to:
- Securely create accounts, log in, and manage diversified portfolios (stocks, cryptocurrencies, mutual funds)
- Access real-time market data using Alpha Vantage API and yfinance
- Receive AI-driven investment recommendations based on individual risk profiles
- Track investment performance over time
- Visualize asset allocations and receive diversification suggestions

Modules
Core Files:
The core files form the backbone of the application. app.py is the main entry point that initializes the Flask app and registers all the Blueprints from different modules. The config.py file holds all the configuration settings, such as database connection strings, email server details, and secret keys. The extensions.py file is used to initialize and manage Flask extensions like SQLAlchemy, Flask-Migrate, and Flask-Mail. The requirements.txt file lists all the Python libraries required to run the project.


Users
Functionality: User Authentication & Profiles  
Responsibilities:
- Manages user registration, login, profile management, and password security.

Portfolio
Functionality: Portfolio Asset Management  
Responsibilities:
- Handles CRUD operations for stocks, cryptocurrencies, and mutual funds.
- Tracks asset valuations and updates.

 Market Data
Functionality:Real-Time Market Data  
Responsibilities:
- Integrates with Alpha Vantage and yfinance APIs to fetch live market prices.

Strategies
Functionality: AI Investment Strategies  

Performance
- Calculates ROI, risk metrics, and generates investment performance charts.

What I Learned
- How to effectively consume API keys and manage API rate limits.
- Real-time market data handling using external APIs like Alpha Vantage API and yfinance.
Issues and Blockers
 API Rate Limiting
Free API services like Alpha Vantage have strict call limits (e.g., 5 calls per minute), which can restrict real-time updates and require careful request management.

How to Run This Project
1.Go to the project folder.
2.Set Up Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3.Install Flask and Other Dependencies:
   ```bash
   pip install Flask
   pip install Flask-SQLAlchemy Flask-Migrate Flask-Login python-dotenv psycopg2-binary requests yfinance
   ```
4.Freeze Requirements:
   ```bash
   pip freeze > requirements.txt
   ```
5.Set Up Flask File Structure.
6.Set Up Database.
7.create a `.env` File with necessary environment variables.
8.Initialize and Migrate the Database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
9.Run the Project:
   ```bash
   python app.py
   ```

Attachments
GitHub Repository Link: 
[https://github.com/pra-nali1812/Wealth_management_portfolio](https://github.com/pra-nali1812/Wealth_management_portfolio)
