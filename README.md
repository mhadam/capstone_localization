# Sensor Localization project
This is a collection of scripts written to processing data from several wireless sensors. The data can be used to localize certain sensors based on received signal strength indicators (RSSI).

## Scripts
* graph.py: used for creating scatter plots of each data set.
* process.py: removes all erroneous data and converts the raw text file data into clean CSVs.
* process_separate_tx.py: takes raw data and sorts each sensor reading into a file according to the sensor it was collected from.
