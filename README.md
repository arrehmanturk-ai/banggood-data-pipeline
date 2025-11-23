# 🛒 Banggood E-commerce Data Pipeline

> Scrape, clean, analyze, and visualize product data from Banggood automatically

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-2019-red.svg)](https://www.microsoft.com/en-us/sql-server)

## What This Does

This project automatically:
1. Scrapes product data from Banggood (prices, ratings, reviews)
2. Cleans messy data (removes $, converts text to numbers)
3. Stores everything in SQL Server database
4. Creates charts and finds insights
5. Gives business recommendations

**Result:** 229 products analyzed with actionable insights worth $50K+ in potential revenue

## Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/banggood-pipeline.git
cd banggood-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python scripts/scraper.py      # Step 1: Scrape
python scripts/cleaner.py      # Step 2: Clean
python scripts/sql_loader.py   # Step 3: Load to DB
python scripts/analysis.py     # Step 4: Analyze
```

## What You Need

- Python 3.9+
- SQL Server 2016+
- Chrome browser
- 4GB RAM

## Project Structure

```
banggood-pipeline/
├── data/
│   ├── banggood_raw.csv          # Scraped data
│   └── banggood_cleaned.csv      # Cleaned data
├── scripts/
│   ├── scraper.py                # Web scraping
│   ├── cleaner.py                # Data cleaning
│   ├── sql_loader.py             # Database loader
│   └── analysis.py               # Analysis & charts
├── sql/
│   └── queries.sql               # 12 SQL queries
├── visualizations/               # Generated charts
└── requirements.txt              # Dependencies
```

## Key Features

✅ Automated web scraping with error handling  
✅ Complete data cleaning pipeline  
✅ SQL Server integration  
✅ 12+ analytical SQL queries  
✅ 5+ professional visualizations  
✅ Business recommendations

## What I Found

### Quick Stats
- **229 products** analyzed
- **Average rating:** 4.12/5 (pretty good!)
- **Price range:** $3.99 - $179.99
- **78.6%** have 4+ star ratings

### Interesting Insights
- 52% of products are budget-friendly (<$20)
- Medium-priced items have highest ratings
- Found 23 "hidden gems" (great products, few reviews)
- Reviews matter more than price for popularity

### Business Impact
If recommendations are implemented:
- 10-15% conversion increase
- $50K-$75K additional revenue
- 20% more customer reviews

## Sample Queries

**Find top products:**
```sql
SELECT TOP 10 Name, Category, Popularity_Score
FROM Products
ORDER BY Popularity_Score DESC;
```

**Average price by category:**
```sql
SELECT Category, AVG(Price_Clean) AS AvgPrice
FROM Products
GROUP BY Category;
```

See `sql/queries.sql` for all 12 queries!

## Technologies Used

- **Scraping:** Selenium, BeautifulSoup
- **Processing:** Pandas, NumPy
- **Database:** SQL Server, PyODBC
- **Visualization:** Matplotlib, Seaborn

## Common Issues

**ChromeDriver not found?**
```bash
# Download ChromeDriver for your Chrome version
# Windows: choco install chromedriver
# Mac: brew install chromedriver
```

**SQL connection failed?**
```python
# Update server name in sql_loader.py
server = r"YOUR_SERVER_NAME"
```

**Module not found?**
```bash
pip install -r requirements.txt --force-reinstall
```

## Contributing

Found a bug? Want to add a feature? Pull requests welcome!

1. Fork the repo
2. Create your branch (`git checkout -b cool-feature`)
3. Commit changes (`git commit -m 'Add cool feature'`)
4. Push to branch (`git push origin cool-feature`)
5. Open a Pull Request

## License

MIT License - feel free to use this for your own projects!

## Author

**Your Name**  
📧 your.email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

## Acknowledgments

Thanks to:
- Banggood for accessible product data
- Python data science community
- Everyone who helped debug my code at 2am 😅

---

**Project Status:** ✅ Complete  
**Last Updated:** November 2025  
**Time Invested:** ~40 hours from idea to final report

---

⭐ Star this repo if you found it helpful!
