#!/bin/bash
git add .
read -p "Commit description: " desc
git commit -m "$desc"
git push https://Camarbro:pflc1234@github.com/Camarbro/Carlitos_Beta.git
