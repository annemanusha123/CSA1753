
h(a,5).
h(b,3).
h(c,4).
h(d,2).
h(e,0).

edge(a,b).
edge(a,c).
edge(b,d).
edge(c,d).
edge(d,e).

best_first(Node, Goal) :-
    write(Node), nl,
    Node = Goal.

best_first(Node, Goal) :-
    edge(Node, Next),
    h(Next, H1),
    h(Node, H2),
    H1 < H2,
    best_first(Next, Goal).
