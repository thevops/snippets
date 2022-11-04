# AWS CLI

> gdate is for macOS

Get current costs (daily)
```bash
╰─❯ aws ce get-cost-and-usage \
 --time-period Start=$(gdate +"%Y-%m-")01,End=$(gdate +"%Y-%m-%d") \
 --granularity=DAILY \
 --metrics BlendedCost \
 --query "ResultsByTime[].[TimePeriod.Start, Total.BlendedCost.[Amount][0], Total.BlendedCost.[Unit][0]]" \
 --output text
2022-11-01	36.9364758515	USD
2022-11-02	23.51343421	USD
2022-11-03	14.956362187	USD
```


Get current costs (monthly)
```bash
aws ce get-cost-and-usage \
 --time-period Start=$(gdate +"%Y-%m-")01,End=$(gdate +"%Y-%m-%d") \
 --granularity=MONTHLY \
 --metrics BlendedCost \
 --query "ResultsByTime[].[TimePeriod.Start, Total.BlendedCost.[Amount][0], Total.BlendedCost.[Unit][0]]" \
 --output text
 ```
