# Rosa's Pizza Notebook-to-Streamlit Skill

## Purpose

Convert the analysis from the Rosa's Pizza Jupyter Notebook into a Streamlit web application.

The notebook is the source of truth for the analytical logic. Preserve the calculations and business logic already developed in the notebook rather than creating a different analytical approach.

## Assignment Context

This application is part of BUSADMIN O712, Data Analytics with Python, Assignment 1: Finding the Best Delivery Promise for Rosa's Pizza.

The purpose of the app is to help Rosa decide the best promised delivery time for each combination of delivery zone and time block.

The application should use the starter package supplied with the assignment.

## Source of Truth

Use the existing notebook and starter package.

The starter package provides:

- ZONES
- TIME_BLOCKS
- COSTS
- PROMISE
- delivery_times()

Do not create replacement versions of these objects.

Do not modify the starter package.

The notebook already contains the analytical functions developed in Part I and Part II.

In particular, reuse the logic from:

- cost_per_late_order()
- best_promise()

## Part II(b) Logic

The notebook calculates the cost of one late order as:

refund cost + (churn orders × profit margin)

The notebook's best_promise() function:

1. Takes a zone.
2. Takes a time block.
3. Takes a list of promised delivery times.
4. Takes the costs dictionary.
5. Simulates delivery times using delivery_times().
6. Counts total orders using len(times).
7. Counts late orders using (times > promise).sum().
8. Calculates net profit as:

   profit from all orders - cost of late orders

9. Compares the net profit for every promise.
10. Returns the promise with the highest net profit.

Preserve this logic in the Streamlit application.

## Promise Range

The notebook uses:

20, 25, 30, ..., 80 minutes

as the current range tested for the recommendation.

The notebook explains that the range was chosen because:

- Very short promises can produce substantial late-order costs.
- Very long promises reduce customer demand.
- The range should be wide enough that the optimal promise is not simply the first or last value tested.
- If the best promise occurs at an endpoint, the range should be expanded.

The Streamlit application should allow the user to set the range of promised delivery times.

Promise values must be tested in 5-minute increments.

Do not hard-code the recommended promise of 55 minutes.

The app must calculate the recommendation dynamically.

## Streamlit User Inputs

The application must allow the user to:

1. Select a zone from ZONES using a dropdown.
2. Select a time block from TIME_BLOCKS using a dropdown.
3. Set the minimum promised delivery time.
4. Set the maximum promised delivery time.
5. Adjust the profit margin per order.
6. Adjust the estimated number of future orders lost after a late order.
7. Adjust the refund cost per late order.
8. Click a button to calculate the recommended promise.

## Streamlit Output

After the user clicks the calculation button, display:

- The selected zone.
- The selected time block.
- The recommended promised delivery time.
- The maximum net profit.

The recommended promise should be calculated from the user's selected inputs.

Do not hard-code the notebook's test result.

## Reproducibility

The assignment explains that delivery_times() is a simulator and can produce different results on different runs.

The notebook uses a seed for reproducibility.

Use the same seed approach from the notebook when converting the logic to Streamlit.

Do not introduce a different simulation method.

## Starter Package

The Streamlit application must import the starter package rather than recreating the assignment data.

The application should use:

from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

The application's requirements.txt must include the rosa-starter package so that Streamlit Community Cloud can install it.

## Coding Style

Keep the implementation simple and appropriate for a beginner Python/data analytics course.

Use:

- Python functions
- loops
- if statements where appropriate
- lists
- dictionaries
- NumPy where needed
- Streamlit for the web interface

Avoid unnecessary libraries or complicated programming patterns.

## Important Constraints

Do not:

- Create new ZONES.
- Create new TIME_BLOCKS.
- Create a replacement COSTS dictionary.
- Create a replacement delivery_times() function.
- Modify the starter package.
- Change the definition of a late order.
- Change the net-profit calculation.
- Hard-code the recommended promise.
- Hard-code the $1,212 result.
- Invent additional business assumptions.
- Replace the notebook's analytical logic with a different optimization method.

## Conversion Approach

When converting the notebook:

1. Inspect the existing notebook first.
2. Identify the Part II(b) best_promise() logic.
3. Reuse that logic in the Streamlit application.
4. Add Streamlit input controls around the existing logic.
5. Keep the calculation separate from the user-interface code where practical.
6. Test the app using the notebook's Far West / Fri/Sat eve example.
7. Make sure the app can also calculate recommendations for other zone/time-block combinations.

The goal is to convert the notebook analysis into an interactive decision-support application while preserving the original assignment logic.
