# serverless-tucan
AWS-based tool notifying about your personal TUCaN grade changes via E-Mail / SES. Readme is WIP.

## Prerequirements
TL;DR: AWS account, installed serverless and aws toolchain (don't forget to `aws configure`)

## Initial Setup
1. `git submodule update --init`

2. Create a 2-line `user-credentials.txt` file on root level with just your credentials inside:
```
<TU-ID>
<PASSWORD>
```

3. Open `serverless.yml` and fill in your desired receiver mail address for `recipientMailAddress` and your sender address for `senderMailAddress` on the very top. You must have access to both addresses (see next step), but keep in mind that the mails *might* be categorized as spam by your provider if both addresses equal.

4. If you don't asked for a SES limit increase yet you need confirm both your sender and receiver address from the step before: https://docs.aws.amazon.com/en_pv/ses/latest/DeveloperGuide/verify-email-addresses-procedure.html

5. `./create-templates.sh`

6. `sls deploy`

Now you are all set and should receive an initial mail with all of your grades exactly one hour after deployment!
