def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    if speed > 60 and speed <= 80:
      return 1
    if speed > 80:
      return 2
  if is_birthday:
    if speed <= 65:
      return 0
    if speed > 65 and speed <= 85:
      return 1
    if speed > 85:
      return 2
