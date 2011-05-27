def is_prime?(num)
  start = Time.now
  if num == 2 or num == 3
    return true
  end
  if num < 2 or num % 2 == 0 or num % 3 == 0
    return false
  end
  (5..Math.sqrt(num).to_i).each do |i|
    return false if num % i == 0
  end
  puts "#{num} in #{Time.now - start}"
  true
end

start_num = 600851475143

Math.sqrt(start_num).to_i.downto(0).each do |num|
  if start_num % num == 0 and is_prime?(num)
    puts num
    break
  end
end
