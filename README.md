# Beaver Image Classifier 

## Business Understanding
Motion activated cameras are great for monitoring wildlife, however, they produce large amounts of data that takes hours to process. As part of my volunteer work with the Eastside Audubon Society, I have a growing dataset of wildlife images for a beaver monitoring project. The goal of this project is to build an image classifier to help sort the data. 

## Data Understanding
From a shared DropBox account I have access to over 2,000 photos from two motion activated cameras. Building a classifier is feasible with transfer learning, as 2,000 images is a small dataset in terms of image classification. I downloaded the data from DropBox and currently store it on my laptop. The goal is to store it in an S3 bucket using Amazon Web Services or other cloud platform. 

Photos were taken between April and June 2019 with Browning and Reconyx cameras. They are mostly grayscale because beavers are more active at night. A majority of the animals in the photos are beavers, however there are also several bird species, frogs, raccoons, rats, rabbits, and squirrels. Photos are either approximately 5376 by 2034 pixels (Browning) by or 2048 by 1152 pixels (Reconyx). Many animals are small, blurry, occluded, or truncated. 

## Data Preparation
Data was downloaded as zipfile from Dropbox. I used Photos on Mac to correct dates and times, and ExifRenamer to rename all photos by the following method:
* name of site (s1)
* name of camera (c1 = Reconyx, c2 = Browning)
* date (year, month, day, hour, minute, second)


I sorted the images into two folders:
* beaver
* not beaver

I used Tensorflow to construct a labeled and shuffled dataset. Data was resized to 224 x 224.  

## Modeling
I used the MobileNetV2 pre-trained model to train my model. 

## Evaluation
I used accuracy and cross-entropy loss to evaluate my model. The next steps would be to reiterate model with different pre-trained models and final layers/steps (maybe output latent features and use random forest or logistic regression as final classification step), set up an input pipeline for new data, determine best storage strategy for all data, and expand to include other metrics.

Once all of that is complete, I would like to move on from an image classifier to a beaver tail object detector. One of the long term goals of this beaver project is to determine the feasibility of beaver identification using wildlife camera photos of beaver tails. I think a reasonable next step is building a machine learning algorithm to select all of the photos with clear instances of beaver tails. Actually for this project I set out to build a beaver object detector, but was unsuccessful. I wanted to start with an object detector so that I could include all categories (not just beaver or not beaver) and get numbers of category instances. I didn't feel like I could do that with a classifier because my data would be too imbalanced. For example, there are maybe 5 photos that have both a beaver and a frog in them, which would make it another, really small, category. I switched to a classifier to have a minimum value product and hope to better learn the tools I was working with so that I can build an object detector. 

## Deployment
This classifier is not designed for deployment.

