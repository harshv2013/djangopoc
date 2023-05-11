from faker import Faker

fake = Faker()

# for _ in range(10):
#    print(fake.name()) 

# print(fake.date_between(start_date="-3y",end_date="-1y")) # date between 2018 and 2020
# print(fake.month())
# print(fake.date_time())
# print(fake.year())
# print(fake.month_name())
# print(fake.date_time_this_year())
# print(fake.time())
# print(fake.timezone())
# print(fake.day_of_week())
# print(fake.time_object())


# print(fake.simple_profile())

print(fake.text()) # news
# print(fake.texts())

print('##########################################################')

print(fake.sentence()) # weather
# print(fake.sentences())