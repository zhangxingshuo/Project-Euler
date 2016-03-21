#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

function isPal(n)
  str = string(n)
  return str == reverse(str)
end

max = 0
for x in range(0,999)
  for y in range(0,999)
    product = x*y
    if product > max && isPal(product)
      max = product
    end
  end
end
print(max)
