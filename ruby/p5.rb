=begin
i = 20
loop do
  if i % 5 == 0 and i % 3 == 0
    if i % 1000000 == 0
      puts i
    end
    result = true
    (2..20).each do |x|
      if i % x != 0
        result = false
        break
      end
    end
    if result
      break
    end
  end
  i += 2
end

puts i
=end
