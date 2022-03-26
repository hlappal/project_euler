STARTING_YEAR = 1900
STARTING_MONTH = 1
STARTING_DAY = 1
STARTING_WKD = 1

SUNDAY_COUNT = 0

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

function is_leap_year(year)
    leap_year = false
    if year % 100 == 0  # is century
        if year % 400 == 0  # is leap year
            leap_year = true
        end
    else  # is not century
        if year % 4 == 0  # is leap year
            leap_year = true
        end
    end
    return leap_year
end

function next_day(year, month, day, wkd)
    months = copy(MONTHS)
    if is_leap_year(year)
        months[2] = 29
    end
    if day < months[month]
        day += 1
    else  # end of month
        if month < 12
            month += 1
        else  # end of year
            year += 1
            month = 1
        end
        day = 1
    end
    if wkd < 7
        wkd += 1
    else
        wkd = 1
    end
    return year, month, day, wkd
end

year = copy(STARTING_YEAR)
month = copy(STARTING_MONTH)
day = copy(STARTING_DAY)
wkd = copy(STARTING_WKD)

MONTH_NAMES = ["Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec"]
DAY_NAMES = ["Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday" "Sunday"]

while year < 1901
    global year, month, day, wkd = next_day(year, month, day, wkd)
end
println("Starting from ", year, " ", MONTH_NAMES[month], " ", day, ", which is a ", DAY_NAMES[wkd])
while year < 2001
    global year, month, day, wkd = next_day(year, month, day, wkd)
    if day == 1 && wkd == 7
        println("Sunday fell on ", day, " ", MONTH_NAMES[month], " ", year)
        global SUNDAY_COUNT += 1
    end
end
println("Ended at ", year, " ", MONTH_NAMES[month], " ", day, ", which is a ", DAY_NAMES[wkd])
println(SUNDAY_COUNT, " Sundays fell on the 1st of a month")
