# Heloc Predictor Project

This project focus on creating a detail analysis and machine learning for decision making predictions based on [MSTZ Heloc Dataset](https://huggingface.co/datasets/mstz/heloc) huggingface.co.

# Purpose of the project

Heloc lending process improvement is becoming a standard practice for financial institutions. With a precise understanding of the data and given predictions on loan approvals, the bank can improve its decision-making process to minimize risk and streamline approvals. We decided to engage in this project because we believe it's an excellent opportunity and a real-world example to enhance our data science skills with tangible outcomes.

# Team

| Name          | Description                        | Github Account | LinkedIn                                                                      |
| ------------- | ---------------------------------- | -------------- | ----------------------------------------------------------------------------- |
| Santiago Paiz | Software Engineer & Data Scientist | @aaoeclipse    | [santiago-paiz-7b2a7268](https://www.linkedin.com/in/santiago-paiz-7b2a7268/) |
| Alex "Andru Andrushevich | Software Engineer & Data Scientist | @QuantGeekDev | [alex-andrushevich-5544845a](https://www.linkedin.com/in/alex-andrushevich-5544845a/) |

# Installation

1. Download [MSTZ Heloc Dataset](https://huggingface.co/datasets/mstz/heloc) into a data/ folder in the root of the project
2. Install python dependencies

```bash
python3 -m pip install -r requirements.txt
```

# Setup

1. Follow the steps in the installation
2. setup mlflow with the correct database

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

3. Run the analysis.ipynb
