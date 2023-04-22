how_much = input('How much does this car cost?');
credit = input('What is your credit score?');

price = int(how_much);
credit_score = int(credit);

if credit_score >= 700:
    print(f'Since your credit score is {credit_score} your down payment will be {price * 0.15}');
elif credit_score <= 699:
    print(f'Since your credit score is {credit_score} your down payment will be {price * 0.27}');