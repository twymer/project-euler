def is_palindrome?(val)
  val.to_s == val.to_s.reverse
end

largest = 0
(100..999).each do |i|
  i.times do |j|
    largest = [largest, i*j].max if is_palindrome? i*j
  end
end

puts largest
