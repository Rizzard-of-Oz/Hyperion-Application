def say_number(num):
    # Define a dictionary of words for numbers up to 99
    ones_and_tens = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    # Define a list of words for the powers of 1000
    powers = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
              'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion',
              'decillion']

    # Convert num to string and split into groups of 3 digits (starting from the right)
    num_str = str(num)[::-1]
    groups = [num_str[i:i+3][::-1] for i in range(0, len(num_str), 3)]

    # Initialize result string
    result = ''

    # Iterate over groups of 3 digits, starting from the highest power of 1000
    for i, group in enumerate(reversed(groups)):
        # Convert group to integer
        group_num = int(group)

        if group_num == 0:
            # Skip empty groups
            continue

        # Convert the hundreds digit to words (if non-zero)
        if group_num >= 100:
            result += ones_and_tens[group_num // 100] + ' hundred '
            group_num %= 100

        # Convert the last two digits to words (tens and ones)
        if group_num in ones_and_tens:
            # If the number is in the ones_and_tens dictionary, use it
            result += ones_and_tens[group_num]
        else:
            # Otherwise, build the word from the tens and ones digits separately
            tens = group_num // 10 * 10
            ones = group_num % 10
            result += ones_and_tens[tens] + ('-' if ones > 0 else '') + ones_and_tens[ones]

        # Add the power of 1000 to the result, if any
        if i > 0 and group_num > 0:
            result += ' ' + powers[i]

        # Add a comma if there are more groups to come
        if i < len(groups) - 1 and int(groups[i+1]) > 0:
            result += ', '

    # Add a period to the end of the result
    result += '.'

    return result
