# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 'and' when writing out numbers is in compliance with British usage.

digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
          6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

tens = {10: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

def num_to_string(num):
    thousand_str = ''
    hundred_str = ''
    tens_str = ''
    ones_str = ''

    if num >= 1000:
        thousand_str += digits[num // 1000] + ' thousand'
        num %= 1000

    if num >= 100:
        hundred_str +=  digits[num // 100] + ' hundred'
        num %= 100

    if num >= 20:
        tens_str += tens[num // 10]
        num %= 10
    if num >= 10:
        tens_str += tens[num]
        num = 0

    if num > 0:
        ones_str += digits[num]
    
    tip = ' '.join([thousand_str, hundred_str]).strip()
    tail = '-'.join([tens_str, ones_str]).strip('-')
    return f'{tip} and {tail}' if len(tip) > 0 and len(tail) > 0 else max(tip, tail)

def count_letters(num_string):
    return len(num_string.replace(' ', '').replace('-', ''))

print(sum(count_letters(num_to_string(num)) for num in range(1, 1001)))
