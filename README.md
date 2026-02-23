Subscription Billing & Status Evaluation Engine
>>Project Overview
This project implements a Subscription Billing Engine in Python that processes subscription and usage data to:
-Calculate monthly bills
-Evaluate final subscription status
-Generate billing outputs
-Produce summary metrics
-Handle invalid data safely
-Provide full unit test coverage

>>Processing Scope
-Only March 2024 usage is considered.
-CANCELLED subscriptions are not billed.
-Subscriptions with no usage → usage defaults to 0.
-Invalid records are skipped and logged.
-Application never crashes due to bad data.

>>Business Rules
1️. Usage Aggregation
-Aggregate total usage per subscription for March 2024.
-Invalid dates are ignored.

2️. Billing Rules
Condition	         Billing Result
usage ≤ limit	     total_bill = monthly_fee
usage > limit	     monthly_fee + (overage_gb × 10)
status = SUSPENDED	 bill monthly_fee only
status = CANCELLED	 bill = 0

3️. Status Evaluation Rules
Condition	                         Final Status
usage > 150% of limit	             SUSPENDED
previous SUSPENDED & usage ≤ limit	 ACTIVE
CANCELLED	                         Never changes

>>Transformations
For each subscription, system generates:
-total_usage_gb
-overage_gb
-total_bill
-final_status

>>Error Handling & Logging:
-Invalid dates are skipped.
-Missing numeric values default safely.
-All errors logged using Python logging.
-Application runs end-to-end without crashing.

▶How to Run the Application

From project root:

python src/main.py

Output files will be generated automatically.

>>Running Unit Tests

python -m unittest discover tests

Test categories covered:
-Billing Logic Tests
-Status Evaluation Tests
-Usage Aggregation Tests

All mandatory test case names are implemented.