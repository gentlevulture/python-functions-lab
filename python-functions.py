# Challenge 1

def sum_to(num):
  total = 0
  for n in range(1, num + 1):
    total += n
  return total

print(sum_to(6)) # returns 21
print(sum_to(10)) # returns 55

# Challenge 2

def largest(lst):
  return max(lst)

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

# alt947
# def largest(nums):
#   nums.sort()
#   return nums[-1]

# Challenge 3

# Challenge 4
