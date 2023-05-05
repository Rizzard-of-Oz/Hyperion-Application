def test_sayNumber():
    # Test basic numbers
    assert sayNumber(0) == "Zero."
    assert sayNumber(11) == "Eleven."
    assert sayNumber(50) == "Fifty."
    assert sayNumber(100) == "One hundred."
    assert sayNumber(120) == "One hundred and twenty."
    assert sayNumber(999) == "Nine hundred and ninety nine."
    
    # Test numbers with trailing zeroes
    assert sayNumber(10) == "Ten."
    assert sayNumber(1000) == "One thousand."
    assert sayNumber(1000000) == "One million."
    assert sayNumber(1000000000) == "One billion."
    
    # Test numbers with multiple digits
    assert sayNumber(987654321) == "Nine hundred and eighty seven million, six hundred and fifty four thousand, three hundred and twenty one."
    assert sayNumber(1000000000000) == "One trillion."
    assert sayNumber(100100100) == "One hundred million, one hundred thousand and one hundred."
    
    # Test large numbers
    assert sayNumber(999999999999999) == "Nine hundred and ninety nine trillion, nine hundred and ninety nine billion, nine hundred and ninety nine million, nine hundred and ninety nine thousand and nine hundred and ninety nine."
    assert sayNumber(123456789012345) == "One hundred and twenty three trillion, four hundred and fifty six billion, seven hundred and eighty nine million, twelve thousand and three hundred and forty five."
    
    print("All test cases passed")
