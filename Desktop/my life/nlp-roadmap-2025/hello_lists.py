# hello_lists.py

# لیست اسامی
names = ["walden", "thoreau", "pond", "concord", "cabin"]

# لیست اعداد
nums = [42, 7, 5, 99, 13]

# نمایش نام‌ها
print("Original names:", names)

# نمایش نام‌های مرتب شده
print("Sorted names:", sorted(names))

# نمایش اعداد اصلی
print("Original nums:", nums)

# مرتب‌سازی معکوس اعداد
nums.sort(reverse=True)
print("Nums desc:", nums)
