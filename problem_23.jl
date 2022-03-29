function get_divisors(n)
    divisors = zeros(0)
    d = 1
    while d < abs(n)
        if n % d == 0
            append!(divisors, d)
        end
        d += 1
    end
    return divisors
end

function number_perfectness(n)
    # Determine if a number is deficient, perfect, or abundant
    s = sum(get_divisors(n))
    if s < n
        # Number is deficient
        return -1
    elseif s > n
        # Number is abundant
        return 1
    else
        # Number is perfect
        return 0
    end
end

function main()
    # First find all abundant numbers below 28124
    abundant_numbers = zeros(0)
    for n in 1:28123
        if number_perfectness(n) == 1
            append!(abundant_numbers, n)
        end
    end
    # Find all abundant number pair sums below 28124
    abundant_sums = zeros(0)
    for i in 1:length(abundant_numbers)
        for j in 1:i
            ij_sum = Int64(abundant_numbers[i] + abundant_numbers[j])
            if ij_sum < 28124 && !(ij_sum in abundant_sums)
                append!(abundant_sums, ij_sum)
            end
        end
    end
    # Find all numbers below 28124 that are not in the list and sum them up
    sum = 0
    for n in 1:28123
        if !(n in abundant_sums)
            sum += n
        end
    end
    println(sum)
end

main()