# 5063 TGN
Case = int(input())
for i in range(Case):
    non_ad_income, ad_income, ad_cost = map(int, input().split())
    if non_ad_income < (ad_income-ad_cost):
        result = "advertise"
    elif non_ad_income == (ad_income-ad_cost):
        result = "does not matter"
    elif non_ad_income > (ad_income-ad_cost):
        result = "do not advertise"
    print(result)
