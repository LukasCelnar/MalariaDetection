# **MalariaDetection**

## **What is this and what is it doing ?**

Model that detects whether human cell is Parasitized with Malaria or Uninfected from given image

Model scored 93.74% accuracy on ± 1000 validation images

Model uses pretrained model Mobilenet V2 from tensorflow hub https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/4

Fully trained model is saved in models/ directory with name: "model-03_12-07.10.2020.h5"

## **How it works ?**

You give it image of size 224px x 244px and you will get true label, predicted label and how confident model is with this prediction

Here is an example:

![example img](/markup_imgs/confusion_matrix.png)

## **Confusion Matrix**

Here is an Confusion Matrix describing performence on validation dataset which contains ± 1000 images

![confusion metrix](/markup_imgs/prediction_example.jpg)

## **What is an Confusion Matrix ? You may ask**

Good question, here is simple explanation from https://www.geeksforgeeks.org/confusion-matrix-machine-learning/

> Confusion matrix is a table that is often used to describe the performance of a classification model (or “classifier”) on a set of test data for which the true values are known. It allows the visualization of the performance of an algorithm.

Or in other words it allows us to see where is our model getting confused
