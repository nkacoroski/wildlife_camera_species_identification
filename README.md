# Wildlife Camera Data Management System and Species Photo Identification Algorithm

## Business Understanding
The Eastside Audubon Society is exploring the use of wildlife cameras to better understand local beaver populations, and are also interested in documenting other wildlife observed. Motion activated cameras are great for monitoring wildlife because they are unobtrusive to animals and expand the window of observation time. They produce large amounts of data, however, which is a time-consuming task to process. The goal of this project is twofold, (1) construct a data management system for long term storage and automated manipulation of image data, and (2) develop an algorithm to detect animals in photos and classify by species.

## Data Understanding
In April 2019, two wildlife cameras (Browning -link- and Reconyx -link-) were installed around a beaver lodge on Lake Sammamish in Redmond, WA. To maximize capture of beavers, cameras were focused on areas of recent beaver activity (scent mounds, mud walls, dams, lodges) near or at the shoreline. Camera settings were experimented with throughout the first few months. To maximize capture of wildlife images, cameras were set at high sensitivity, with 10 photos per trigger and the smallest setting between photo capture (Browning = 1 sec, Reconyx = no setting -check with camera-). There is the possibilty of additional data sources as the Eastside Audubon Society would like to set up wildlife cameras around other beaver lodges on Lake Sammamish.

## Data Preparation
### Data Collection and Storage
Photos are collected weekly (if possible) and uploaded as zip files. During data collection, beaver activity at camera locations is evaluated and cameras are moved if necessary to more recent beaver activity around the lodge. Initially, image data was uploaded to Dropbox, in September 2019, image data was moved to Azure blob storage. A select group of volunteers have access to the account and upload the zip files of raw images each week as new blobs to "raw_image_data." Labels for zip files are as follows:
* date (YYYYMMDD)
* name of site (s1)
* name of camera (c1 = Reconyx, c2 = Browning)

### Data Cleaning
Currently image data is cleaned manually and then stored as blobs of individual image blobs under "cleaned_image_data." The following tasks are done to clean images.
* correct datetime (no longer necessary, but datetime was incorrect on ... from April 2019 to ...)
* rename all images by site, camera, and datetime (wildlife cameras give duplicate names each week to photos)
* crop images to eliminate automatic wildlife labels (this information is not useful and could be misleading to computer vision algorithms)

### Data Annotations

### Exploratory Data Analysis


I used Tensorflow to construct a labeled and shuffled dataset. Data was resized to 224 x 224.  

## Modeling
I used the MobileNetV2 pre-trained model to train my model. 

## Evaluation
I used accuracy and cross-entropy loss to evaluate my model. The next steps would be to reiterate model with different pre-trained models and final layers/steps (maybe output latent features and use random forest or logistic regression as final classification step), set up an input pipeline for new data, determine best storage strategy for all data, and expand to include other metrics.

Once all of that is complete, I would like to move on from an image classifier to a beaver tail object detector. One of the long term goals of this beaver project is to determine the feasibility of beaver identification using wildlife camera photos of beaver tails. I think a reasonable next step is building a machine learning algorithm to select all of the photos with clear instances of beaver tails. Actually for this project I set out to build a beaver object detector, but was unsuccessful. I wanted to start with an object detector so that I could include all categories (not just beaver or not beaver) and get numbers of category instances. I didn't feel like I could do that with a classifier because my data would be too imbalanced. For example, there are maybe 5 photos that have both a beaver and a frog in them, which would make it another, really small, category. I switched to a classifier to have a minimum value product and hope to better learn the tools I was working with so that I can build an object detector. 

## Deployment
This classifier is not designed for deployment.

