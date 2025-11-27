using Printf
using DataFrames, Gadfly, Colors, Cairo, Fontconfig

function haldane(s, low, high)
    p = low
    q = 1-p
    x = log(p/q)
    t = 0
    w11 = 1 + s
    w12 = 1 + s/2

    # Haldane's formula
    t = (2/s)*log( (high/(1-high)) / (low/(1-low)) )
    print("Expected t: $t")
    print()

    tvec = Vector{Float64}()
    sizehint!(tvec, Int(round(t+100)))

    pvec = Vector{Float64}()
    sizehint!(pvec, Int(round(t+100)))

    xvec = Vector{Float64}()
    sizehint!(xvec, Int(round(t+100)))

    push!(tvec, t)
    push!(pvec, p)
    push!(xvec, x)

    @printf("%5d %7.4f %7.4f\n", t, p, x)

    while p < high
        wbar = 1 + p*s
        #print("wbar=$wbar w11=$w11 w12=$w12")
        p *= (p*w11 + q*w12)/wbar
        q = 1-p
        x = log(p/q)
        t += 1

        push!(tvec, t)
        push!(pvec, p)
        push!(xvec, x)
        @printf("%5d %7.4f %7.4f\n", t, p, x)
    end

    pplt = plot(x=tvec, y=pvec, Geom.line,
                color=[colorant"black"],
                Guide.xlabel("t (generations)"),
                Guide.ylabel("p(t)", orientation=:horizontal),
                Guide.title("Allele frequency"),
                Theme(plot_padding=[3mm]),
                Coord.cartesian(aspect_ratio=2))
        
    xplt = plot(x=tvec, y=xvec, Geom.line,
                color=[colorant"black"],
                Guide.xlabel("t (generations)"),
                Guide.ylabel("x(t)", orientation=:horizontal),
                Guide.title("Logit transform of allele frequency"),
                Theme(plot_padding=[3mm]),
                Coord.cartesian(aspect_ratio=2))
    
    plt =  hstack(pplt, xplt)

    plot_name = @sprintf("plogit-%g-%g-%g.pdf", s, low, high)
    draw(PDF(plot_name; dpi=300), plt)

    return nothing
end
