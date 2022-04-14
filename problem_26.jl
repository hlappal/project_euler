function get_recip(d)
    r = 1/d
    rn = r
    for i in 1:10
        rn *= 10
        println(rn)
    end

    return rn
end

function main()
    d = 7
    recip = get_recip(d)
    println(d, " has a recurring decimal cycle ", recip)
end

main()
