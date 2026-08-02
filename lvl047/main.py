# 1) შექმენით lambda ფუნქცია double, რომელიც არგუმენტად მიიღებს რიცხვს და პასუხად დააბრუნებს გაორმაგებულს.

double = (lambda x : 2*x)(9)
print(double)

# 2) შექმენით lambda ფუნქცია check_odd, რომელიც შეამოწმებს რიცხვი კენტია თუ არა.
#  თუ კენტია - აბრუნებს True-ს. სხვა შემთხვევაში False-ს.

check_odd = (lambda y : y % 2 != 0)(2)

print(check_odd)