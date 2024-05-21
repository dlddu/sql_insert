#!/bin/bash

mysql -u root -ptpce -D tpce -h db < 1_create_table.sql &&
mysql -u root -ptpce -D tpce -h db < 1.5_enable_load_local_data.sql &&
mysql -u root -ptpce -D tpce -h db --local-infile=1 < 2_load_data.sql &&
mysql -u root -ptpce -D tpce -h db < 3_create_index.sql &&
mysql -u root -ptpce -D tpce -h db < 4_create_fk.sql &&
mysql -u root -ptpce -D tpce -h db < 5_create_sequence.sql
