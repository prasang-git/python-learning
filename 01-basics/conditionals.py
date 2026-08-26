age = 20
has_id = False

if age >= 18 and has_id:
    print("You can enter.")
elif age >= 18 and not has_id:
    print("You need an ID.")
else:
    print("You are not eligible.")