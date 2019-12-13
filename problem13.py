# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open('problem13.txt', 'r') as num_txt:
    nums = [int(num) for num in num_txt.readlines()]
    sum_of_nums = sum(nums)
    print(str(sum_of_nums)[:10])
