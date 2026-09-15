# ============================================================
# Exercise 2: Create a timeline of Iranian cities
# ============================================================

import json

# Load data (after Exercise 1)
with open("exercise1_result.json", "r", encoding="utf-8") as f:
    iran_cities = json.load(f)

# Create timeline
timeline = {}

for city in iran_cities["شهرها"]:
    period = city["دوره_تاسیس"]
    if period not in timeline:
        timeline[period] = []
    timeline[period].append(city["نام"])

# Sort chronologically
period_order = [
    "دوره هخامنشی (منطقه)",
    "دوره ساسانیان",
    "دوره سامانیان",
    "دوره صفوی (به عنوان پایتخت)",
    "دوره قاجار (به عنوان پایتخت)"
]

sorted_timeline = {}
for period in period_order:
    if period in timeline:
        sorted_timeline[period] = timeline[period]

# Save
with open("exercise2_timeline.json", "w", encoding="utf-8") as f:
    json.dump(sorted_timeline, f, indent=2, ensure_ascii=False)

print(" Exercise 2 complete! Saved to exercise2_timeline.json")
print("\nTimeline:")
for period, cities in sorted_timeline.items():
    print(f"  {period}: {', '.join(cities)}")
