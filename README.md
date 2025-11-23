# AI Ethics Assignment: Designing Responsible and Fair AI Systems

**Author:** Peter Mwaura
**GitHub:** [https://github.com/Phitah02](https://github.com/Phitah02)

## Overview
This repository contains the submission for the AI Ethics Assignment, focusing on "Designing Responsible and Fair AI Systems." The assignment evaluates understanding of AI ethics principles, bias identification and mitigation, and application of ethical frameworks to real-world scenarios. It includes theoretical questions, case study analyses, a practical bias audit of the COMPAS dataset, ethical reflections, and a bonus policy proposal.

The assignment is structured into four main parts plus a bonus task, implemented individually but aligned with group collaboration guidelines. The original assignment questions are detailed in `AI Ethics Assignment.docx`.

## Project Structure
```
.
├── AI Ethics Assignment.docx      # Original assignment questions and guidelines
├── AI Development workflow Answers.pdf  # Written answers for Parts 1, 2, 4, and Bonus Task
├── Part 3/                        # Practical audit deliverables (Part 3)
│   ├── compas_analysis.ipynb      # Jupyter notebook for COMPAS bias audit
│   ├── compas_analysis.py         # Python script version of the audit
│   ├── REPORT.md                  # 300-word report on COMPAS findings
│   ├── compas-scores-two-years.csv # COMPAS dataset (sourced from ProPublica)
│   ├── fpr_fnr_disparity.png      # Visualization: FPR/FNR disparities
│   └── recidivism_comparison.png  # Visualization: Actual vs predicted recidivism
├── bonus.md                       # Bonus: Ethical AI guidelines for healthcare (additional copy)
└── README.md                      # This file
```

## Tools and Libraries
- **AI Fairness 360 (AIF360)**: IBM's toolkit for bias detection and mitigation.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Matplotlib & Seaborn**: Data visualization.
- **Jupyter Notebook**: Interactive code execution.
- **Scikit-learn**: Machine learning utilities (used in AIF360).

## Datasets
- **COMPAS Recidivism Dataset**: Obtained from [ProPublica's COMPAS Analysis Repository](https://github.com/propublica/compas-analysis.git). The file `compas-scores-two-years.csv` is stored in `Part 3/` and used for auditing racial bias in recidivism risk scores.

## Assignment Parts Overview
The assignment is divided into four parts plus a bonus task, as outlined in `AI Ethics Assignment.docx`.

- **Part 1: Theoretical Understanding (30%)**: Short answer questions and ethical principles matching. See `AI Development workflow Answers.pdf` for responses.
- **Part 2: Case Study Analysis (40%)**: Analysis of biased hiring tool and facial recognition cases. See `AI Development workflow Answers.pdf` for detailed solutions.
- **Part 3: Practical Audit (25%)**: Bias audit of COMPAS dataset using AIF360. Deliverables in `Part 3/` folder, including code, visualizations, and report.
- **Part 4: Ethical Reflection (5%)**: Personal reflection on ensuring ethical AI in projects. See `AI Development workflow Answers.pdf`.
- **Bonus Task (Extra 10%)**: Policy proposal for ethical AI in healthcare. See `bonus.md` and `AI Development workflow Answers.pdf`.

## Submission Details
- **Written Answers**: Parts 1, 2, 4, and Bonus Task are in `AI Development workflow Answers.pdf`.
- **Code & Visualizations**: Part 3 (Practical Audit) deliverables are in the `Part 3/` folder, including code, report, and visualizations.
- **Assignment Questions**: Refer to `AI Ethics Assignment.docx` for the original prompts.
- **Group Collaboration**: While implemented individually, aligns with peer group guidelines for shared learning.

## Grading Alignment
- **Theoretical Accuracy (30%)**: Covered in Part 1.
- **Case Study Depth & Solutions (40%)**: Detailed in Part 2.
- **Technical Audit Execution (25%)**: Implemented in Part 3.
- **Reflection & Creativity (5%)**: Provided in Part 4.

## Why This Matters
Ethical AI prevents societal harm, builds trust, and is a key skill for AI careers. This assignment demonstrates practical application of fairness principles using real tools and datasets.

## References
- ProPublica: COMPAS Analysis (https://github.com/propublica/compas-analysis)
- IBM AI Fairness 360 (https://github.com/IBM/AIF360)
- EU Ethics Guidelines for Trustworthy AI

For questions, join the PLP Academy Community discussion: #AIEthicsAssignment.
