cache = Dict(1 => 1, 2 => 1)

function fib(n)
    if get(cache, n, 0) > 0
        return cache[n]
    end
    # if n < 3
    #     return 1
    # else
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
    # end
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
    # fibs = [1, 1]
    # i = 2
    # id = 1
    # dmax = 1
    # diffs = []
    # while true
    #     fibs = [fibs[2], fibs[1] + fibs[2]]
    #     i += 1
    #     d = digits(fibs[2])
    #     if d > dmax
    #         diff = i - id
    #         append!(diffs, diff)
    #         id = i
    #         dmax = d
    #         println("The largest number of digits increase to ", dmax, " at ", i, "'th Fibonacci number ", fibs[2])
    #         #println("Difference: ", diff)
    #         #println("The first to have ", 1e9, " digits is the ", i, "'th Fibonacci number ", fibs[2])
    #     end
    #     if dmax > 101
    #         break
    #     end
    # end
    #println(diffs)
    i = 1
    while true
        n = fib(i)
        d = digits(n)
        if d == 20
            println("The first to have ", d, " digits is the ", i, "'th Fibonacci number ", n)
            break
        end
        #println("The ", i, "'th Fibonacci number ", n, " has ", d, " digits")
        i += 1
    end
end

main()
