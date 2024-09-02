def sell_tickets():
    total_tickets = 20  # total available tickets
    total_buyers = 0  # accumulator for total number of buyers

    while total_tickets > 0:
        # input: Asking the user for the number of tickets they want to purchase
        tickets_requested = int(input("How many tickets would you like to buy? (Max 4 per buyer): "))

        # if statement to check if the requested number of tickets is valid
        if tickets_requested < 1 or tickets_requested > 4:
            print("You can only buy between 1 and 4 tickets.")
            continue

        # if statement to check if there are enough tickets remaining
        if tickets_requested > total_tickets:
            print(f"Sorry, only {total_tickets} tickets are remaining.")
            continue

        # output: show the number of tickets remaining after purchase
        total_tickets -= tickets_requested
        total_buyers += 1
        print(f"Tickets remaining: {total_tickets}")

    # Output: display total number of buyers
    print(f"All tickets sold! Total number of buyers: {total_buyers}")

# calling the function to execute the ticket selling process
sell_tickets()
