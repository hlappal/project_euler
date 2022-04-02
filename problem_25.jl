function fib(n)
    if n < 3
        return 1
    else
        return fib(n-1) + fib(n-2)
    end
end

function digits(n)
    if n < 1
        return 0
    else
        d = 1
        i = 10
        while (n / i) > 1
            d += 1
            i *= 10
        end
        return d
    end
end

function main()
    i = 1
    while true
        n = fib(i)
        d = digits(n)
        if d == 3
            println("The first to have ", d, " digits is the ", i, "'th Fibonacci number ", n)
            break
        end
        #println("The ", i, "'th Fibonacci number ", n, " has ", d, " digits")
        i += 1
    end
end

main()
