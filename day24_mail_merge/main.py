friends = ["Ross", "Rachael", "Phoebe", "Chandler", "Joey", "Monica"]

for friend in friends:
    with open(f"day24_mail_merge/letter_for_{friend}.txt", mode="w") as file:
        file.write(
            f"Dear {friend},\n\nYou are invited to my birthday party on Saturday.\n\nHope you can make it!\n\nAngela"
        )
