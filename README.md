# Carbon Emission & Sink Analyzer (CESA)

## Overview
This project focuses on analyzing satellite imagery to estimate carbon emissions and carbon sink potential using computer vision and machine learning techniques.

The system uses a U-Net based semantic segmentation model to identify vegetation and land-cover patterns, followed by machine learning models to estimate carbon sequestration.

## Key Features
- Satellite image segmentation using U-Net
- Land-cover classification
- Carbon emission and sink estimation
- End-to-end ML pipeline from preprocessing to inference
- Visualization of results

## Tech Stack
- Python
- TensorFlow / PyTorch
- U-Net (Semantic Segmentation)
- XGBoost, Random Forest
- NumPy, Pandas, Matplotlib

## Workflow
1. Data collection (satellite imagery)
2. Data preprocessing and augmentation
3. Model training (U-Net for segmentation)
4. Feature extraction from segmented output
5. Carbon estimation using ML models
6. Visualization and analysis

## Challenges Faced
- Noisy and inconsistent satellite data
- Class imbalance in land-cover categories
- Model generalization across regions

## Results
- Achieved ~50% IoU for segmentation
- Approximate ±12% accuracy in carbon estimation
- Built a working pipeline for real-world geospatial analysis

## Future Improvements
- Improve segmentation accuracy with advanced architectures
- Integrate Vision Transformers
- Optimize for real-time inference
- Deploy as a scalable web application

## Note
This project was developed as part of academic/research exploration and demonstrates end-to-end ML system design.
