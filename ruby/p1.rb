puts (1...1000).reject{ |num| num % 3 != 0 and num % 5 != 0 }.inject(0) { |sum, num| sum + num }
