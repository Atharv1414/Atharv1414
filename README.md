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
| [**Withyreach Hotel**](https://github.com/Atharv1414/withyreach-hotel) · [live](https://atharv1414.github.io/withyreach-hotel/) | Hotel website whose sky, colours and theme follow the real sun | 42 unit and component tests, 12 browser tests | React, JavaScript, SCSS |
| [**Lantern Hall**](https://github.com/Atharv1414/lantern-hall) · [live](https://atharv1414.github.io/lantern-hall/) | Theatre box office where a seat can never be sold twice | 60 buyers race for 24 seats in the tests | React, FastAPI, MongoDB |
| [**Open Desk**](https://github.com/Atharv1414/ai-support-desk) · [live](https://atharv1414.github.io/ai-support-desk/) | AI support desk with a fine-tuned model, cited answers and a guarded agent | The release gate rejected my own fine-tuned model, and the write-up says why | React, Python, LoRA, RAG, MySQL |
| [**NYC Congestion Pricing Impact**](https://github.com/Atharv1414/nyc-congestion-pricing-impact) | Tests whether New York's congestion charge sped up traffic, on 128 million real taxi trips | +3.1% in 2025, fading from +5.9% to +1.4%, with a placebo year that tests the method | Python, DuckDB, causal inference |
| [**A/B Test Meta-Analysis**](https://github.com/Atharv1414/ab-test-meta-analysis) | Learns how to run experiments from 32,487 real A/B tests | Winners claim +61% and deliver +27%; shrinkage predicts +26% | Python, empirical Bayes |
| [**Retail Customer Value**](https://github.com/Atharv1414/retail-customer-value) | Warehouse and customer value forecasts on a million real invoice lines | Top-rated fifth brought 76% of the next six months' revenue | dbt, DuckDB, Python |
| [**Azure Handbook RAG**](https://github.com/Atharv1414/azure-handbook-rag) | Answers questions about company documents with checked citations | 30 tests and an evaluation set; not yet deployed to live Azure | Python, Azure AI Search, Azure AI Foundry |
| [**Broadband Support Agent**](https://github.com/Atharv1414/daily-projects/tree/main/broadband-support-agent) | Support agent with policy rules, human approval and injection guardrails | 26-case evaluation suite graded on actions taken | Python, Claude tool use, Pydantic |
| [**Traffic Light Optimisation**](https://github.com/Atharv1414/traffic-light-optimisation) | Vision pipeline that adapts signal timings to queues | In simulation: 0% to 28.9% more vehicles served, 12% to 93% less delay | YOLOv8, OpenCV |
| [**Web Scraping Data Pipeline**](https://github.com/Atharv1414/daily-projects/tree/main/web-scraping-pipeline) | Fault-tolerant ETL with retries, validation and quarantine | Live run loaded 1,100 records in 52 s | Python, MySQL |
| [**Warehouse Stock Reservation API**](https://github.com/Atharv1414/warehouse-stock-reservation-api) | Holds stock safely when many orders compete for it | 3,000-reservation load test with no unit oversold | C#, ASP.NET Core, EF Core |
| [**Factory Telemetry Historian**](https://github.com/Atharv1414/factory-telemetry-historian) | Time-series storage engine with crash recovery | 6.1x compression: 2.63 bytes per sample against 16 raw | C++20, CMake |

The congestion pricing, A/B test and retail projects use real public data. Other datasets are synthetic unless a project says otherwise.

## See it running

| [Withyreach Hotel](https://atharv1414.github.io/withyreach-hotel/) | [Lantern Hall](https://atharv1414.github.io/lantern-hall/) |
|---|---|
| [<img src="https://raw.githubusercontent.com/Atharv1414/withyreach-hotel/main/docs/home-dusk.png" alt="Hotel home page at dusk over a reedbed" width="400">](https://atharv1414.github.io/withyreach-hotel/) | [<img src="https://raw.githubusercontent.com/Atharv1414/lantern-hall/main/docs/seats.png" alt="Theatre seat map with three seats chosen" width="400">](https://atharv1414.github.io/lantern-hall/) |
| Click to open the live site | Click to open the live site (demo mode) |

**Traffic Light Optimisation:** identical simulated traffic, with fixed timing on the left. On the right, YOLOv8 counts the queues and sets the greens.

[![Two simulated junctions side by side. The adaptive one serves more vehicles and has a shorter queue.](https://raw.githubusercontent.com/Atharv1414/traffic-light-optimisation/main/docs/demo.gif)](https://github.com/Atharv1414/traffic-light-optimisation)

| [Grocery Retail BI Mart](https://github.com/Atharv1414/daily-projects/tree/main/grocery-retail-bi-mart) | [E-commerce Marketing Attribution](https://github.com/Atharv1414/daily-projects/tree/main/ecommerce-marketing-attribution) |
|---|---|
| <img src="https://raw.githubusercontent.com/Atharv1414/daily-projects/main/grocery-retail-bi-mart/docs/images/dashboard.png" alt="Trading dashboard with KPI cards and monthly sales against target" width="400"> | <img src="https://raw.githubusercontent.com/Atharv1414/daily-projects/main/ecommerce-marketing-attribution/docs/charts/roas_by_model.png" alt="Bar chart showing that return on ad spend by channel depends on the attribution model" width="400"> |
| Star schema, semantic layer and row-level security, with 18 reconciliation checks | dbt on DuckDB: six attribution models compared, with 79 dbt tests |

## Latest projects

<!-- latest:start -->
| Added | Project | Role | Built with |
|---|---|---|---|
| 24 Nov 2026 | [Azure Handbook RAG](https://github.com/Atharv1414/daily-projects/tree/main/azure-handbook-rag) | AI Engineer | Python, Azure AI Search, Azure AI Foundry, Entra ID, Bicep |
| 24 Nov 2026 | [Damp & Mould Repairs Business Case](https://github.com/Atharv1414/daily-projects/tree/main/damp-mould-repairs-business-case) | Business Analyst | Python, process mining + conformance checking |
| 24 Nov 2026 | [Law Firm Profitability BI](https://github.com/Atharv1414/daily-projects/tree/main/law-firm-profitability-bi) | BI Developer | Python, DuckDB, price-volume-mix, FastAPI, Plotly |
| 24 Nov 2026 | [Factory Telemetry Historian](https://github.com/Atharv1414/daily-projects/tree/main/factory-telemetry-historian) | Data Engineer | C++20, CMake, GoogleTest, WAL crash recovery |
| 23 Nov 2026 | [E-commerce Marketing Attribution](https://github.com/Atharv1414/daily-projects/tree/main/ecommerce-marketing-attribution) | Data Analyst | SQL, sessionisation, ASOF identity stitching |
| 23 Nov 2026 | [Streaming QoE Pipeline](https://github.com/Atharv1414/daily-projects/tree/main/streaming-qoe-pipeline) | Data Engineer | Python, event-time stream processing |

14 projects in the series so far: Data Engineer 3 · Agentic AI Engineer 2 · BI Developer 2 · Business Analyst 2 · Data Analyst 2 · Software Engineer 2 · AI Engineer 1.
<!-- latest:end -->

More in [**daily-projects**](https://github.com/Atharv1414/daily-projects), a growing collection across software, data, analytics and AI.

## By role

- **Front end and full stack:** [Withyreach Hotel](https://github.com/Atharv1414/withyreach-hotel) · [Lantern Hall](https://github.com/Atharv1414/lantern-hall) · [Open Desk](https://github.com/Atharv1414/ai-support-desk)
- **Software engineering:** [Candid Blog](https://github.com/Atharv1414/daily-projects/tree/main/candid-blog) · [Expense Tracker](https://github.com/Atharv1414/daily-projects/tree/main/expense-tracker-cli) · [French Lingo](https://github.com/Atharv1414/daily-projects/tree/main/french-lingo)
- **AI and agents:** [Open Desk](https://github.com/Atharv1414/ai-support-desk) · [Hotel Revenue SQL Agent](https://github.com/Atharv1414/daily-projects/tree/main/hotel-revenue-sql-agent) · [Azure Handbook RAG](https://github.com/Atharv1414/azure-handbook-rag)
- **Data engineering:** [Smart Meter Lakehouse](https://github.com/Atharv1414/daily-projects/tree/main/smart-meter-lakehouse) · [Streaming QoE Pipeline](https://github.com/Atharv1414/daily-projects/tree/main/streaming-qoe-pipeline)
- **Data analysis:** [NYC Congestion Pricing](https://github.com/Atharv1414/nyc-congestion-pricing-impact) · [A/B Test Meta-Analysis](https://github.com/Atharv1414/ab-test-meta-analysis) · [Retail Customer Value](https://github.com/Atharv1414/retail-customer-value) · [NHS Outpatient DNA Analysis](https://github.com/Atharv1414/daily-projects/tree/main/nhs-outpatient-dna-analysis) · [E-commerce Marketing Attribution](https://github.com/Atharv1414/daily-projects/tree/main/ecommerce-marketing-attribution)
- **Business intelligence:** [Grocery Retail BI Mart](https://github.com/Atharv1414/daily-projects/tree/main/grocery-retail-bi-mart) · [Law Firm Profitability BI](https://github.com/Atharv1414/daily-projects/tree/main/law-firm-profitability-bi)
- **Business analysis:** [Motor Claims Business Case](https://github.com/Atharv1414/daily-projects/tree/main/motor-claims-fnol-business-case) · [Damp and Mould Repairs](https://github.com/Atharv1414/daily-projects/tree/main/damp-mould-repairs-business-case)

## Toolkit

- **Languages:** Python · SQL · JavaScript · HTML · SCSS · C# · C++ · Dart
- **Front end:** React · Vite · Vitest · Playwright · accessibility testing with axe
- **Data:** pandas · NumPy · DuckDB · dbt · MySQL · MongoDB · SQLite · Plotly
- **AI:** Claude tool use · agents with guardrails · RAG · LoRA fine-tuning · MLOps · LLM evaluation · scikit-learn · PyTorch · YOLOv8 · Azure AI Search
- **Engineering:** Flask · FastAPI · ASP.NET Core · Flutter · Docker · GitHub Actions · pytest · AI-assisted development with Claude Code
