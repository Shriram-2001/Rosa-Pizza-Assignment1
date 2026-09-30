import streamlit as st

from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times


SEED = 1


def cost_per_late_order(costs):
    return costs["refund"] + costs["churn_orders"] * costs["margin"]


def best_promise(zone, time_block, promises, costs):
    late_cost = cost_per_late_order(costs)

    best_promise_so_far = None
    best_profit_so_far = None

    for promise in promises:
        times = delivery_times(zone, time_block, promise, seed=SEED)

        number_of_orders = len(times)
        number_of_late = (times > promise).sum()

        profit = number_of_orders * costs["margin"] - number_of_late * late_cost

        if best_profit_so_far is None or profit > best_profit_so_far:
            best_promise_so_far = promise
            best_profit_so_far = profit

    return best_promise_so_far, best_profit_so_far


st.set_page_config(page_title="Rosa's Pizza Promise Calculator", page_icon="🍕")
st.title("Rosa's Pizza Delivery Promise")
st.write("Find the promised delivery time with the highest estimated net profit.")

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

st.subheader("Promises to test")
range_col1, range_col2 = st.columns(2)
with range_col1:
    minimum_promise = st.number_input(
        "Minimum promised time (minutes)",
        min_value=5,
        value=20,
        step=5,
    )
with range_col2:
    maximum_promise = st.number_input(
        "Maximum promised time (minutes)",
        min_value=5,
        value=80,
        step=5,
    )

st.subheader("Costs")
margin_col, churn_col, refund_col = st.columns(3)
with margin_col:
    margin = st.number_input(
        "Profit margin per order ($)",
        min_value=0.0,
        value=float(COSTS["margin"]),
        step=1.0,
    )
with churn_col:
    churn_orders = st.number_input(
        "Future orders lost after a late order",
        min_value=0,
        value=int(COSTS["churn_orders"]),
        step=1,
    )
with refund_col:
    refund = st.number_input(
        "Refund cost per late order ($)",
        min_value=0.0,
        value=float(COSTS["refund"]),
        step=1.0,
    )

if st.button("Calculate best promised time", type="primary"):
    if minimum_promise > maximum_promise:
        st.error("The minimum promised time must not exceed the maximum.")
    elif minimum_promise % 5 != 0 or maximum_promise % 5 != 0:
        st.error("Choose minimum and maximum times in 5-minute increments.")
    else:
        promises_to_try = list(range(int(minimum_promise), int(maximum_promise) + 1, 5))
        user_costs = COSTS.copy()
        user_costs["margin"] = margin
        user_costs["churn_orders"] = churn_orders
        user_costs["refund"] = refund

        recommended_promise, maximum_net_profit = best_promise(
            zone,
            time_block,
            promises_to_try,
            user_costs,
        )

        st.write(f"**Zone:** {zone}")
        st.write(f"**Time block:** {time_block}")
        result_col1, result_col2 = st.columns(2)
        result_col1.metric("Recommended promised time", f"{recommended_promise} minutes")
        result_col2.metric("Maximum net profit", f"${maximum_net_profit:,.2f}")

        if recommended_promise == promises_to_try[0] or recommended_promise == promises_to_try[-1]:
            st.info("The best result is at the edge of this range. Consider testing a wider range.")