#!/bin/bash

input_file="transactions.csv"
output_file="normalized_transactions.csv"

# Remove lines with missing values
awk -F, 'NF==7' $input_file > temp.csv

# Normalize date format to ISO 8601
awk -F, '{ if (NR == 1) { print $0 } else { "date -d \""$2"\" +%Y-%m-%dT%H:%M:%SZ" | getline date; $2 = date; OFS=","; print $0 } }' temp.csv > $output_file

# Clean up
rm temp.csv
