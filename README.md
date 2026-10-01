# Learning Analytics Portfolio

Reproducible examples of learning and engagement analytics using **fully synthetic data**.

This repository demonstrates how I structure learning-activity data, define practical KPIs, analyze engagement and conversion, and turn operational records into decision-support outputs. It contains no proprietary, employer, client, student, or member data.

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

The analysis script reads the synthetic activity file and reports:

1. total activity records;
2. unique participants and active organizations;
3. attendance and completion conversion rates;
4. activity by quarter;
5. activity by topic; and
6. activity by delivery format.

## Portfolio note

In professional settings, I work with substantially larger and more complex datasets. Public examples are rebuilt with synthetic or de-identified data so that the analytical methods can be evaluated without exposing confidential information.

## Areas for extension

Planned additions include cohort retention, year-over-year comparison, utilization scoring, organization segmentation, dashboard-ready output tables, and a synthetic learning-portfolio recommendation model.

---

**Laura Elizabeth Hand**  
[Portfolio](https://www.lauraelizabethhand.com/) · [LinkedIn](https://www.linkedin.com/in/lauraelizabethhand)
