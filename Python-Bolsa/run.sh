#!/bin/bash
python getDataYahoo.py $1
python trataData.py
python trataData2.py


