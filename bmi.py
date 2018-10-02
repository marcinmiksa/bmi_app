def bmi_counter(height=2.0, weight=90):
    try:
        bmi = height/weight
        return bmi
    except ZeroDivisionError:
        return None


print(bmi_counter(2, 0))
