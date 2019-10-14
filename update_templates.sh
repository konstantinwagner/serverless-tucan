#!/bin/sh

echo "Creating templates..."
aws ses create-template --region us-east-1 --cli-input-json file://assets/templates/newgrades.json
aws ses create-template --region us-east-1 --cli-input-json file://assets/templates/error.json

echo ""
echo "+------------------------------------------------+"
echo "| Errors while creation (above) are totally fine |"
echo "| as long as template updates below succeed      |"
echo "+------------------------------------------------+"
echo ""
echo "Updating templates..."
aws ses update-template --region us-east-1 --cli-input-json file://assets/templates/newgrades.json
aws ses update-template --region us-east-1 --cli-input-json file://assets/templates/error.json
