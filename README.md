# Ettuthogai Poem Classification and Semantic Analysis

This project identifies whether a given Tamil poem belongs to the Ettuthogai corpus
(specifically Agananuru subset) and performs semantic analysis using NLP techniques.

## Features
- Ettuthogai vs Non-Ettuthogai poem classification (ML-based)
- Corpus-based fallback validation
- Tamil Unicode handling
- Entity extraction and simplified meaning generation

## How to Run

```bash
pip install scikit-learn pandas tensorflow numpy
python create_dataset.py
python train_validator.py
python main.py
