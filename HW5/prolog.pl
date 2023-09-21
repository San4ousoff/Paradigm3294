% Правило, когда список пустой
sum_list([], 0).

% Правило, когда список не пустой,
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, Rest),
    Sum is Head + Rest.

% Вызов
?- sum_list([1, 2, 3, 4, 5], X), write(X).