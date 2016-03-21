#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

function factor(n)
  factors = [1]
  pop!(factors)
  i = 2
  while i^2 <= n
    if n%i != 0
      i += 1
    else
      push!(factors,i)
      n /= i
    end
  end
  if n > 1
    push!(factors,round(Int,n))
  end
  return factors
end

arr = factor(600851475143)
print(arr[length(arr)])
