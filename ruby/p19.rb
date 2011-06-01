require 'Date'

count = 0

1901.upto(2000) do |year|
  1.upto(12) do |month|
    # Date.civil defaults to first day of month
    if Date.civil(year, month).wday == 0
      count += 1
    end
  end
end

puts count
