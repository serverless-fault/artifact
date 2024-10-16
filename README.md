# README

### The script and dataset of serverless-related faults

##### We downloaded all the data on December 19, 2023

``Dataset``  --- the dataset of GitHub projects, SO posts, and GitHub Issues

$\qquad$ ```Collect & Filter Projects.xlsx``` -- the dataset of 2,489 candidate projects and 10 selected projects in the end

$\qquad$ ```Extracted_Issues.xlsx``` -- the 3,157 issues extracted from selected projects. The *Whether_Selected* column indicates whether this issue is selected or not.

$\qquad$ ```Extracted_Posts.xlsx``` -- the 6,748 raw posts collected from Stack Overflow

$\qquad$ ```Annotated_Dataset.xlsx``` -- the manually labeled 593 faults and the result of characteristics comparison

```GitHub_Code``` --- the script to collect, filter projects and extract and filter issues

$\qquad$ ```filter.py``` -- the script to filter candidate projects by number of stars, forks, and contributors

$\qquad$ ```get_issues.py``` -- the script to extract issues from selected projects

$\qquad$ ```README.md``` -- the tutorial to collect data from GitHub

```SO_Code``` --- the script to collect SO posts

$\qquad$ ```README.md``` -- the tuorial to collect data from Stack Overflow
