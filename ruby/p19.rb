# A lot simpler than my python try.. didn't have to
# use any personal checking of day of week or if it
# is a leapyear
require 'Date'

count = 0

# Date.civil defaults to first day of month
1901.upto(2000) do |year|
  1.upto(12) do |month|
    if Date.civil(year, month).wday == 0
      count += 1
    end
  end
end

puts count
