# hour = ur_time // 3600
# minute = ur_time // 60
# seconds = ur_time % 60
# print(f"{hour:.1f}, {minute:.1f}, {minute_h:.1f}")

ur_time = int(input("Введите число в секундах: "))
hour = ur_time // 3600
minute = ur_time // 60 - hour * 60
seconds = ur_time % 60

print(f"{hour:02}:{minute:02}:{seconds:02}")
