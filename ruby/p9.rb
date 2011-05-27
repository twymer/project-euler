1000.times do |b|
  (b - 1).times do |a|
    c = Math.sqrt(a**2 + b**2)
    if c % 1 == 0 and b < c and a + b + c == 1000
      puts "a: #{a}, b: #{b}, c: #{c}"
      puts a*b*c
    end
  end
end



