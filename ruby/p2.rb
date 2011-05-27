def gen_fibs
  fibs = [0,1]
  (1..100).each do |i|
    fibs[i+1] = fibs[i] + fibs[i-1]
  end
  fibs
end

#def gen_fibs2
#  n = 10
#  fibs = [0,1]
#  n.times do |i|
#    fibs[i+1] = fibs[i] + fibs[i-1]
#  end
#  fibs
#end

def gen_fibs3
  fibs = [0,1]
  n = 10
  a,b = 0,1
  (n-1).times do
    a,b = b,a+b
    fibs << b
  end
  fibs
end

def p2
  sum = 0
  max = 4000000
  a,b = 0,1

  while b < max
    sum += b if b % 2 == 0
    a,b = b,a+b
  end
  sum
end

puts p2

