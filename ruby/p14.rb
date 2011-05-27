def next_val(n)
  if n.even?
    n / 2
  else
    3 * n + 1
  end
end

max_chain = 0
max_start = 0
2.upto(1000000) do |i|
  n = i
  chain = 1
  while n > 1
    chain += 1
    n = next_val n
  end
  max_chain, max_start = chain, i if chain > max_chain
end
puts max_chain, max_start

