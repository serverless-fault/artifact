# README

#### To collect data from Stack Overflow


download posts on the Stack Exchange Data Explorer
https://data.stackexchange.com/stackoverflow/queries

##### 1. Download posts with tag "serverless"
input query sentence
```
SELECT * 
FROM Posts
WHERE Tags like '%<serverless>%'
```

##### 2. Download posts with tag "faas"
input query sentence
```
SELECT * 
FROM Posts
WHERE Tags like '%<faas>%'
```
##### 3. Download the results as Excel 
Posts of other tags also are downloaded by similar methods, including *aws-serverless*, *openwhisk*, *serverless-architecture*, *serverless-framework*, *serverless-offline*, *serverless-pulgins*

The downloaded posts are in **Extracted_Posts.xlsx**
