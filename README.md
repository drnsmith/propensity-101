# Propensity 101

This project explores how to model customer response likelihood using logistic regression — known as **propensity scoring**.

While many teams use these models to predict who is likely to convert, this project also surfaces the deeper strategic question: *are we changing behaviour, or just confirming it?*

## 🔍 Techniques Covered
- Logistic regression for binary classification
- Feature engineering with synthetic data
- ROC curve and AUC evaluation
- Ranking customers by propensity score

## 📈 Business Context

This type of analysis is foundational for:
- Smarter campaign targeting
- Reducing spend on customers who would convert anyway
- Laying the groundwork for causal uplift modelling

## 🧪 Dataset

A synthetic dataset of 1000 records with 8 customer features and a binary response variable. Generated with `sklearn.datasets.make_classification`.

## 📁 Folder Structure

- `notebooks/`: Main Jupyter notebook
- `data/`: Synthetic CSV file
- `images/`: Output plots and visuals
