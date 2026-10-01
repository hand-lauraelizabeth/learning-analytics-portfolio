# Learning Analytics Portfolio

[![Validate analysis](https://github.com/hand-lauraelizabeth/learning-analytics-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/hand-lauraelizabeth/learning-analytics-portfolio/actions/workflows/validate.yml)

Reproducible examples of learning and engagement analytics using **fully synthetic data**.

This repository demonstrates how I structure learning-activity data, define practical KPIs, analyze engagement and conversion, and turn operational records into decision-support outputs. It contains no proprietary, employer, client, student, or member data.

## Results at a glance

| Metric | Synthetic result |
| --- | ---: |
| Activity records | 36 |
| Unique participants | 16 |
| Active organizations | 6 |
| Registration → attendance | 81.2% |
| Attendance → completion | 53.8% |

### Activity records by quarter

| Quarter | Records |
| --- | ---: |
| 2026 Q1 | 13 |
| 2026 Q2 | 8 |
| 2026 Q3 | 9 |
| 2026 Q4 | 6 |

### Activity records by topic

| Topic | Records |
| --- | ---: |
| AI for Marketing | 11 |
| Data & Analytics | 7 |
| Brand Strategy | 6 |
| Creative Effectiveness | 5 |
| Measurement | 4 |
| Procurement | 3 |

These are demonstration outputs from the synthetic dataset, not employer or client performance figures.

## What this demonstrates

- Data cleaning and validation
- KPI and metric design
- Participant and organization-level utilization analysis
- Registration-to-attendance and attendance-to-completion conversion
- Quarterly trend analysis
- Topic and delivery-format segmentation
- Reproducible analysis workflows
- Privacy-conscious portfolio development

## Repository structure

```
learning-analytics-portfolio/
├── .github/workflows/
│   └── validate.yml
├── analysis/
│   └── engagement_summary.py
├── data/
│   └── sample_learning_activity.csv
├── docs/
│   └── data_dictionary.md
├── README.md
└── requirements.txt
```

## Quick start

```bash
pip install -r requirements.txt
python analysis/engagement_summary.py
```

The analysis script reads the synthetic activity file and reports total activity, unique participants and organizations, conversion rates, quarterly activity, topic mix, and delivery-format mix.

## Portfolio note

In professional settings, I work with substantially larger and more complex datasets. Public examples are rebuilt with synthetic or de-identified data so the analytical methods can be evaluated without exposing confidential information.

## Areas for extension

Planned additions include cohort retention, year-over-year comparison, utilization scoring, organization segmentation, dashboard-ready output tables, and a synthetic learning-portfolio recommendation model.

---

**Laura Elizabeth Hand**  
[Portfolio](https://www.lauraelizabethhand.com/) · [LinkedIn](https://www.linkedin.com/in/lauraelizabethhand)
