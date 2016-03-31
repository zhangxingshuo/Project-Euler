#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

function pyTrip()
  for a in range(1,500)
    for b in range(1,a)
      c = (a^2 + b^2)^0.5
      if (round(c) == c) & (a+b+c == 1000)
        return a*b*c
      end
    end
  end
  return 0
end

print(pyTrip())
