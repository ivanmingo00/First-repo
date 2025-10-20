weight = 25

destination = "international"

membership = "premium"

base_cost = 10

overweight_surcharge = 5

international_surcharge_multiplier = 2

premium_discount = 0.20

total_cost = base_cost

if weight > 20:

    total_cost += overweight_surcharge

if destination == "international":

    if membership != "premium":

        total_cost *= international_surcharge_multiplier

if membership == "premium":

    total_cost *= (1 - premium_discount)

print(f"Weight (lbs): {weight}")

print(f"Destination (domestic/international): {destination}")

print(f"Membership (standard/premium): {membership}")

print(f"Final Shipping Cost: ({total_cost:.2f}")

details = f"Details: Base ){base_cost}"

if weight > 20:

    details += f" + Overweight ${overweight_surcharge}"

if destination == "international" and membership != "premium":

    details += f", International surcharge applied"

if membership == "premium":

    details += f", Premium {premium_discount*100}% discount applied, International fee waived."

print(f"({details})")