require 'mathn'

def count_divisors(x)
  count = 1
  (2..Math.sqrt(x)).each { |n| count += 1 if x % n == 0 }
  count *= 2 if x > 3
  count
end


current_triangle = 0
i = 1
loop do
  current_triangle += i
  total = count_divisors(current_triangle)
  if  total > 500
    puts current_triangle
    break
  end
  i += 1
end

