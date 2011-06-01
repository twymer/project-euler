# Problem 20
# I really like using inject..

n = 100
factorial = (1..n).inject(:*)
puts factorial.to_s.split(//).inject(0) { |sum, char| sum + char.to_i }
