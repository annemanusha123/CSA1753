
at(monkey, floor).
at(box, floor).
at(banana, ceiling).

can_get_banana :-
    at(monkey, floor),
    at(box, floor),
    write('Monkey walks to the box'), nl,
    write('Monkey pushes the box under the banana'), nl,
    write('Monkey climbs the box'), nl,
    write('Monkey grabs the banana'), nl.
