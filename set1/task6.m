p1 = test(false, 50000)
p2 = test(true, 50000)

function ratio = test(change, n)
    won = 0;
    
    for i = 1:n
        prize = randi(3);
        first_choice = randi(3);
       
        if change == true
            to_show = setdiff(1:3, [prize, first_choice]);
        
            show_ind = randi(size(to_show, 2));
            show = to_show(show_ind);
            last = setdiff(1:3, [first_choice, show]);
            first_choice = last(1);
        end
        
        if prize == first_choice
            won = won + 1.0;
        end
    end
    
    ratio = won / n;
end
