function d(n)
    sum = 0
    for i in 1:n-1
        if n % i == 0
            sum += i
        end
    end
    return sum
end

function main()
    sum = 0
    for n in 1:10000
        a = d(n)
        b = d(a)
        if b == n && b != a
            sum += a
        end
    end
    println("The sum of amicable numbers is ", sum)
end

main()
