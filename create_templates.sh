#!/bin/sh

echo "Creating template..."
aws ses create-template --region us-east-1 --cli-input-json file://assets/templates/newgrades.json

echo ""
echo "Please use the following command for template updates (if an error occurred above):"
echo "# ses update-template --region us-east-1 --cli-input-json file://assets/templates/newgrades.json"
