goal(X):-rule(X).
rule(c):-rule(b).
rule(b):-rule(a).
fact(a).
