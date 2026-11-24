<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Atharv Patil. Software, data and AI engineering." width="100%">
</picture>

I build tested, documented projects that start from a real business problem, from data pipelines and BI marts to LLM agents and mobile apps. The write-ups report what was measured and where each project falls short.

[![tests](https://github.com/Atharv1414/daily-projects/actions/workflows/tests.yml/badge.svg)](https://github.com/Atharv1414/daily-projects/actions/workflows/tests.yml)

## Featured work

| Project | What it does | Highlight | Built with |
|---|---|---|---|
| [**Workout Buddy**](https://github.com/Atharv1414/workout_buddy) | Exercise coach for iOS and Android that counts reps and scores form | Pose detection runs on the device, with no video upload | Flutter, Dart, ML Kit |
| [**NYC Congestion Pricing Impact**](https://github.com/Atharv1414/nyc-congestion-pricing-impact) | Tests whether New York's congestion charge sped up traffic, on 128 million real taxi trips | +3.1% in 2025, fading from +5.9% to +1.4%, with a placebo year that tests the method | Python, DuckDB, causal inference |
| [**A/B Test Meta-Analysis**](https://github.com/Atharv1414/ab-test-meta-analysis) | Learns how to run experiments from 32,487 real A/B tests | Winners claim +61% and deliver +27%; shrinkage predicts +26% | Python, empirical Bayes |
| [**Retail Customer Value**](https://github.com/Atharv1414/retail-customer-value) | Warehouse and customer value forecasts on a million real invoice lines | Top-rated fifth brought 76% of the next six months' revenue | dbt, DuckDB, Python |
| [**Azure Handbook RAG**](https://github.com/Atharv1414/azure-handbook-rag) | Answers questions about company documents with checked citations | 30 tests and an evaluation set; not yet deployed to live Azure | Python, Azure AI Search, Azure AI Foundry |
| [**Broadband Support Agent**](https://github.com/Atharv1414/daily-projects/tree/main/broadband-support-agent) | Support agent with policy rules, human approval and injection guardrails | 26-case evaluation suite graded on actions taken | Python, Claude tool use, Pydantic |
| [**Traffic Light Optimisation**](https://github.com/Atharv1414/traffic-light-optimisation) | Vision pipeline that adapts signal timings to queues | In simulation: 0% to 28.9% more vehicles served, 12% to 93% less delay | YOLOv8, OpenCV |
| [**Web Scraping Data Pipeline**](https://github.com/Atharv1414/daily-projects/tree/main/web-scraping-pipeline) | Fault-tolerant ETL with retries, validation and quarantine | Live run loaded 1,100 records in 52 s | Python, MySQL |
| [**Warehouse Stock Reservation API**](https://github.com/Atharv1414/warehouse-stock-reservation-api) | Holds stock safely when many orders compete for it | 3,000-reservation load test with no unit oversold | C#, ASP.NET Core, EF Core |
| [**Factory Telemetry Historian**](https://github.com/Atharv1414/factory-telemetry-historian) | Time-series storage engine with crash recovery | 6.1x compression: 2.63 bytes per sample against 16 raw | C++20, CMake |

The three analysis projects at the top use real public data. Other datasets are synthetic unless a project says otherwise.

## See it running

**Traffic Light Optimisation:** identical simulated traffic, with fixed timing on the left. On the right, YOLOv8 counts the queues and sets the greens.

[![Two simulated junctions side by side. The adaptive one serves more vehicles and has a shorter queue.](https://raw.githubusercontent.com/Atharv1414/traffic-light-optimisation/main/docs/demo.gif)](https://github.com/Atharv1414/traffic-light-optimisation)

| [Grocery Retail BI Mart](https://github.com/Atharv1414/daily-projects/tree/main/grocery-retail-bi-mart) | [E-commerce Marketing Attribution](https://github.com/Atharv1414/daily-projects/tree/main/ecommerce-marketing-attribution) |
|---|---|
| <img src="https://raw.githubusercontent.com/Atharv1414/daily-projects/main/grocery-retail-bi-mart/docs/images/dashboard.png" alt="Trading dashboard with KPI cards and monthly sales against target" width="400"> | <img src="https://raw.githubusercontent.com/Atharv1414/daily-projects/main/ecommerce-marketing-attribution/docs/charts/roas_by_model.png" alt="Bar chart showing that return on ad spend by channel depends on the attribution model" width="400"> |
| Star schema, semantic layer and row-level security, with 18 reconciliation checks | dbt on DuckDB: six attribution models compared, with 79 dbt tests |

More in [**daily-projects**](https://github.com/Atharv1414/daily-projects), a growing collection across software, data, analytics and AI.

## By role

- **Software engineering:** [Candid Blog](https://github.com/Atharv1414/daily-projects/tree/main/candid-blog) · [Expense Tracker](https://github.com/Atharv1414/daily-projects/tree/main/expense-tracker-cli) · [French Lingo](https://github.com/Atharv1414/daily-projects/tree/main/french-lingo)
- **AI and agents:** [Hotel Revenue SQL Agent](https://github.com/Atharv1414/daily-projects/tree/main/hotel-revenue-sql-agent) · [Azure Handbook RAG](https://github.com/Atharv1414/azure-handbook-rag)
- **Data engineering:** [Smart Meter Lakehouse](https://github.com/Atharv1414/daily-projects/tree/main/smart-meter-lakehouse) · [Streaming QoE Pipeline](https://github.com/Atharv1414/daily-projects/tree/main/streaming-qoe-pipeline)
- **Data analysis:** [NYC Congestion Pricing](https://github.com/Atharv1414/nyc-congestion-pricing-impact) · [A/B Test Meta-Analysis](https://github.com/Atharv1414/ab-test-meta-analysis) · [Retail Customer Value](https://github.com/Atharv1414/retail-customer-value) · [NHS Outpatient DNA Analysis](https://github.com/Atharv1414/daily-projects/tree/main/nhs-outpatient-dna-analysis) · [E-commerce Marketing Attribution](https://github.com/Atharv1414/daily-projects/tree/main/ecommerce-marketing-attribution)
- **Business intelligence:** [Grocery Retail BI Mart](https://github.com/Atharv1414/daily-projects/tree/main/grocery-retail-bi-mart) · [Law Firm Profitability BI](https://github.com/Atharv1414/daily-projects/tree/main/law-firm-profitability-bi)
- **Business analysis:** [Motor Claims Business Case](https://github.com/Atharv1414/daily-projects/tree/main/motor-claims-fnol-business-case) · [Damp and Mould Repairs](https://github.com/Atharv1414/daily-projects/tree/main/damp-mould-repairs-business-case)

## Toolkit

- **Languages:** Python · SQL · C# · C++ · Dart
- **Data:** DuckDB · dbt · MySQL · SQLite · pandas · Plotly
- **AI:** Claude tool use · RAG · LLM evaluation · YOLOv8 · Azure AI Search
- **Engineering:** Flask · FastAPI · ASP.NET Core · Flutter · Docker · GitHub Actions · pytest · AI-assisted development with Claude Code
