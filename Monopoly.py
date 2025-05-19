import random


class Player:
    def __init__(self, name, money=15000, location="Start", in_jail=False, jail_term=0, loc=0, properties = None, locs = None, alimony = 0):
        self.location = location
        self.loc = loc
        self.name = name
        self.money = money
        self.in_jail = in_jail
        self.jail_term = jail_term
        self.properties = properties if properties is not None else []
        self.locs = locs if locs is not None else []
        self.alimony = 0


locations = {
    0: {"name": "Start", "description": "the starting point, Taoyuan International Airport!", "income": 250},
    1: {"name": "Property1", "description": " Taoyuan", "income": 120, "cost": 300},
    2: {"name": "Property2", "description": " Keelung", "income": 96, "cost": 240},
    3: {"name": "Property3", "description": "Taipei 101", "effect":"The first of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    4: {"name": "Property4", "description": "Taipei", "income": 120, "cost": 300},
    5: {"name": "Casino1", "description": "a casino and gambled to win a random effect!", 'income': 0, 'cost': 0,
        "effects": ["Advance to Start", "Money laundering", "Bank pays you $50", "Pay all players $100",
                    "Receive $100 from all players", "Win lottery", "Pay 5% to charity", "Car breaks down", "Property Taxes", "Income Taxes", "Holiday Season"], 'special':'Divorce'},
    6: {"name": "Property6", "description": "New Taipei", "income": 160, "cost": 400},
    7: {"name": "Property7", "description": "National Palace Museum", "effect":"The second of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    8: {"name": "Property8", "description": " Zhubei", "income": 72, "cost": 180},
    9: {"name": "Property9", "description": "Yilan", "income": 48, "cost": 120},
    10: {"name": "Jail", "description": "Jail", 'income': 0, 'cost': 0},
    11: {"name": "Property11", "description": "Taichung", "income": 128, "cost": 320},
    12: {"name": "Property12", "description": "Hsinchu", "income": 104, "cost": 260},
    13: {"name": "Property13", "description": "Taroko National Park", "effect":"The third of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    14: {"name": "Property14", "description": "Miaoli", "income": 48, "cost": 120},
    15: {"name": "Casino2", "description": "a casino and gambled to win a random effect!", 'income': 0, 'cost': 0,
         "effects": ["Advance to Start", "Money laundering", "Bank pays you $50", "Pay all players $100",
                     "Receive $100 from all players", "Win lottery", "Pay 5% to charity", "Car breaks down", "Property Taxes", "Income Taxes", "Holiday Season"], 'special':'Divorce'},
    16: {"name": "Property16", "description": "Toufen", "income": 56, "cost": 140},
    17: {"name": "Property17", "description": "Sun Moon Lake", "effect":"The fourth of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    18: {"name": "Property18", "description": "Hualien", "income": 64, "cost": 160},
    19: {"name": "Property19", "description": "Changhua", "income": 88, "cost": 220},
    20: {"name": "Free Parking", "description": "a Free Parking spot. Nothing really happens here, consider taking a rest.", 'income': 0, 'cost': 0},
    21: {"name": "Property21", "description": "Nantou", "income": 56, "cost": 140},
    22: {"name": "Property22", "description": "Douliu", "income": 56, "cost": 140},
    23: {"name": "Property23", "description": "Yu Shan Jade Mountain", "effect":"The fifth of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    24: {"name": "Property24", "description": "Yuanlin", "income": 72, "cost": 180},
    25: {"name": "Casino3", "description": "a casino and gambled to win a random effect!", 'income': 0, 'cost': 0,
         "effects": ["Advance to Start", "Money laundering", "Bank pays you $50", "Pay all players $100",
                     "Receive $100 from all players", "Win lottery", "Pay 5% to charity", "Car breaks down", "Property Taxes", "Income Taxes", "Holiday Season"], 'special':'Divorce'},
    26: {"name": "Property26", "description": "Magong", "income": 40, "cost": 100},
    27: {"name": "Property27", "description": "Alishan Range", "effect":"The sixth of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    28: {"name": "Property28", "description": "Chiayi", "income": 88, "cost": 220},
    29: {"name": "Property29", "description": "Taibao", "income": 32, "cost": 80},
    30: {"name": "Bank", "description": "Bank", 'income': 0, 'cost': 0},
    31: {"name": "Property31", "description": "Puzi", "income": 32, "cost": 80},
    32: {"name": "Property32", "description": "Tainan", "income": 112, "cost": 280},
    33: {"name": "Property33", "description": "Kaoshiung Love River", "effect":"The seventh of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    34: {"name": "Property34", "description": "Kaoshiung", "income": 140, "cost": 350},
    35: {"name": "Casino4", "description": "a casino and gambled to win a random effect!", 'income': 0, 'cost': 0,
         "effects": ["Advance to Start", "Money laundering", "Bank pays you $50", "Pay all players $100",
                     "Receive $100 from all players", "Win lottery", "Pay 5% to charity", "Car breaks down", "Property Taxes", "Income Taxes", "Holiday Season"], 'special':'Divorce'},
    36: {"name": "Property36", "description": "Kaoshiung International Airport", "effect":"Rumors has it that purchasing this property basically lets you collect airport dividends twice!", "income": 250, "cost": 500},
    37: {"name": "Property37", "description": "Kenting National Park", "effect":"The eigth of eight Views of Taiwan! Rumors has it purchasing multiple Views of Taiwan has certain bonuses!", "income": 200, "cost": 400},
    38: {"name": "Property38", "description": "Taitung", "income": 64, "cost": 160},
    39: {"name": "Property39", "description": "Pingtung", "income": 80, "cost": 200},
}


class CircularQueue:
    def __init__(self):
        self.players = []
        self.order = []
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, player):
        self.players.append(player)
        self.rear = (self.rear + 1) % len(self.players)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.size -= 1
            player = self.players[self.front]
            self.front = (self.front + 1) % len(self.players)
            return player

    def get_front(self):
        return self.players[self.front]

    def is_empty(self):
        return self.size == 0

    def rotate(self):
        if not self.is_empty():
            self.front = (self.front + 1) % len(self.players)

    def remove_property(self, player, property_name):
        if property_name in player.properties:
            player.properties.remove(property_name)
            for p in self.players:
                if property_name in p.properties:
                    p.properties.remove(property_name)
                    break

    def sell_property(self, player):
        if len(player.properties) > 0:
            property_to_sell = player.properties[0]
            property_info = locations[
                next(key for key, value in locations.items() if value["name"] == property_to_sell)]
            property_cost = property_info.get("cost", 0)
            sell_price = int(property_cost * 0.8)
            player.money += sell_price
            self.remove_property(player, property_to_sell)
            print(f"{player.name} sold {property_to_sell} for {sell_price}.")

    def handle_debt(self, player):
        while player.money < 0:
            print(f"{player.name} is in debt with ${player.money}!")
            self.sell_property(player)
            if player.money < 0 and len(player.properties) == 0:
                print(f"{player.name} has no more properties and is eliminated from the game!")
                self.players.remove(player)
                self.order.append(player)
                self.size -= 1
                break

    @staticmethod
    def game_over_condition_met(queue):
        debt_free_players = [player for player in queue.players if player.money >= 0]
        return len(debt_free_players) <= 1

    @staticmethod
    def move_player(current_location, dice_roll, in_jail, jail_term, loc):
        new_position = (loc + dice_roll) % 40
        new_location = locations[new_position]["name"]
        return new_location, in_jail, new_position

    def get_all_bought_properties(self):
        all_bought_properties = []
        for player in self.players:
            all_bought_properties.extend(player.properties)
        return all_bought_properties

def buy_property(player, current_location, loc):
    property_info = locations[loc]
    property_cost = property_info.get("cost", 0)
    property_rent = property_info.get("income", 0)

    if property_cost <= player.money:
        print(f"{player.name} has purchased land in {property_info['description']}")
        if property_info['name'] in ["Property3", "Property7", "Property13", "Property17", "Property23", "Property27", "Property33", "Property37"]:
            print(f"{property_info['effect']}")
        player.money -= property_cost
        player.properties.append(property_info['name'])
        player.locs.append(loc)
    elif property_cost > player.money:
        print(f"{player.name} does not have enough money to purchase land in {property_info['description']} and will need to pay rent for staying there!")
        player.money -= property_rent

def calculate_set_bonus(player):
    property_set = ["Property3", "Property7", "Property13", "Property17", "Property23", "Property27", "Property33", "Property37", "Property36"]
    owned_properties = set(player.properties)
    bonus_multiplier = min(len(owned_properties.intersection(property_set)), 8)
    bonus_income = 0
    rent = 0
    if 1 < bonus_multiplier < 8:
        bonus_income = (bonus_multiplier-1) * 50 * bonus_multiplier
        rent = 200 + (bonus_multiplier-1) * 50
    elif bonus_multiplier == 8:
        bonus_income = 800 * 8
        rent = 800
    return bonus_income, rent

def update_income_tax(player):
    base_tax_percentage = 0.4
    bonus_income, rent = calculate_set_bonus(player)
    property_income = sum(locations[prop]["income"] for prop in player.locs)
    total_income = property_income + bonus_income
    tax = int(total_income * base_tax_percentage)
    return tax, total_income

def casino_effects(player, current_location, loc):
    property_income = 0
    property_cost = 0
    luck = random.randint(1,200)
    if luck != 1:
        effect = random.choice(locations[5]["effects"])
        print(f"{player.name} got: {effect}")
        if effect == "Advance to Start":
            print("You rode the Taiwan High Speed Rail and zoomed through Taiwan arriving in all the way to Taoyuan International Airport!")
            player.money += 100
            dice_roll = 40 - loc
            player.location, player.in_jail, player.loc = CircularQueue.move_player(current_location, dice_roll,
                                                                                     player.in_jail, player.jail_term,
                                                                                     loc)
        elif effect == "Money laundering":
            print(f"{player.name} has been caught money laundering and has to spend 3 turns in jail as well as pay a $500 fine!")
            player.in_jail = True
            player.jail_term = 3
            player.money -= 500
            if loc < 10:
                dice_roll = 5
            elif loc > 10:
                dice_roll = 50 - loc
            player.location, player.in_jail, player.loc = CircularQueue.move_player(current_location, dice_roll,
                                                                                     player.in_jail, player.jail_term,
                                                                                     loc)
        elif effect == "Bank pays you $500":
            print("Your savings account in the bank is ready to cash out! You get $50 from the bank")
            player.money += 500
        elif effect == "Pay all players $100":
            print("You lost a bet to the other players and have to pay them $250")
            for p in players:
                if p != player:
                    p.money += 250
                    player.money -= 250
        elif effect == "Receive $250 from all players":
            print("You were elected as this round's community leader and get to collect $250 in community fees!")
            for p in players:
                if p != player:
                    p.money -= 250
                    player.money += 250
        elif effect == "Win lottery":
            lottery = random.randint(100,2000)
            print(f'You struck big and collected lottery winnings worth ${lottery}!')
            player.money += lottery
        elif effect == "Pay 5% to charity":
            print(f"As the public starts to judge your wealth, you're forced to donate a chunk of your money to charity to appease the raging public!")
            charity = int(player.money * 0.05)
            player.money -= charity
        elif effect == "Car breaks down":
            print("You lost a turn as you are unable to travel anywhere!")
            player.jail_term = 100
        elif effect == "Property Taxes":
            property_cost = sum(locations[prop]["cost"] for prop in player.locs)
            tax = int(property_cost * 0.2)
            player.money -= tax
            print(f"The IRS is suspicious of your property wealth! You need to pay property taxes equal to 20% of your property costs, which is ${tax}.")
        elif effect == "Income Taxes":
            tax, property_income = update_income_tax(player)
            player.money -= tax
            print(f"The IRS isn't too happy with your income statements and found lots of holes in it! You need to pay income taxes equal to 40% of your total income, which is ${tax}.")
        elif effect == "Holiday Season":
            tax, property_income = update_income_tax(player)
            player.money += property_income
            print(
                f"It's the Holiday Season! All your properties are booked! You received money equal to 100% of all your property income, which is ${property_income}.")
    elif luck == 1:
        print(f'{player.name} got married to a golddigger wife without a prenup!!!')
        print('You are now divorced and the court demands you to pay your ex-wife half your total income, half your total money, and half the value of all your properties. For 18 turns, you will also be forced to pay alimony equal to 10% of your total income!')
        half = 0.5 * player.money
        tax, property_income = update_income_tax(player)
        property_cost = sum(locations[prop]["cost"] for prop in player.locs)
        half_income = property_income * 0.5
        half_property = property_cost * 0.5
        total = half + half_property + half_income
        player.money -= int(total)
        print(f'In total, you paid ${half} of your money, ${half_income} in income, and ${half_property} in property cost which totals to ${total}!')
        player.alimony = 18


    return player


def pay_luxury_tax(player):
    luxury_tax = int(player.money * 0.1)
    player.money -= luxury_tax
    print(f"{player.name}, you landed in a bank spot and need to pay luxury tax equal to 10% of your money, which is ${luxury_tax}.")


def simulate_game(players):
    queue = CircularQueue()
    for player in players:
        queue.enqueue(player)

    while not CircularQueue.game_over_condition_met(queue):
        current_player = queue.get_front()
        print(f"\nIt's {current_player.name}'s turn.")
        if current_player.jail_term > 1:
            print(f"{current_player.name} is in jail and has lost a turn!")
        elif current_player.in_jail is False:
            dice_roll = random.randint(1, 6)
            print(f"Dice rolled: {dice_roll}")

            current_location = locations[next(key for key, value in locations.items() if value["name"] == current_player.location)]
            loc = list(locations.values()).index(current_location)
            current_player.location, current_player.in_jail, current_player.loc = CircularQueue.move_player(
                current_location, dice_roll, current_player.in_jail, current_player.jail_term, loc
            )



            location_info = locations[next(key for key, value in locations.items() if value["name"] == current_player.location)]

            if loc + dice_roll > 39:
                if "Property36" in current_player.properties:
                    current_player.money += 500
                    print(f"{current_player.name} passed the starting point and got $500, double the dividends for owning the Kaoshiung International Airport!")
                else:
                    current_player.money += locations[0]["income"]
                    print(f"{current_player.name} passed the starting point and got $250 in dividends!")
            print(
                f"{current_player.name} landed on {location_info['description']}."
            )

        all_bought_properties = queue.get_all_bought_properties()

        if location_info['name'].startswith('Property') and location_info['name'] not in all_bought_properties:
            buy_property(current_player, current_player.loc, current_player.loc)
        elif location_info['name'].startswith('Property') and location_info['name'] in all_bought_properties:
            if location_info['name'] in current_player.properties:
                print(f"{current_player.name} owns this land and will not need to pay rent")
            elif location_info['name'] not in current_player.properties:
                for player in players:
                    if location_info['name'] in player.properties:
                        if location_info['name'] in ["Property3", "Property7", "Property13", "Property17", "Property23", "Property27", "Property33", "Property37"]:
                            bonus_income, rent = calculate_set_bonus(player)
                            rent = rent + 200
                            print(f"{player.name} owns this land, thus {current_player.name} will have to pay rent to {player.name} as much as {rent}")
                            player.money += rent
                            current_player.money -= rent
                        else:
                            print(f"{player.name} owns this land, thus {current_player.name} will have to pay rent to {player.name} as much as {location_info['income']}")
                            current_player.money -= location_info["income"]
                            player.money += location_info["income"]

        if current_player.location == "Jail" and not current_player.in_jail:
            current_player.in_jail = True
            current_player.jail_term = 3

        elif current_player.location == "Jail" and current_player.in_jail:
            current_player.jail_term -= 1
            if current_player.jail_term == 0:
                current_player.in_jail = False
                print(f"{current_player.name} is out of jail!")
                current_player.money -= 100
                print(f"{current_player.name} lost $100 for being in jail.")
        elif current_player.jail_term == 100:
            current_player.jail_term -= 100

        if current_player.location == "Bank":
            pay_luxury_tax(current_player)

        if current_player.location in ("Casino1", "Casino2", "Casino3", "Casino4"):
            casino_effects(current_player, current_player.loc, current_player.loc)

        if current_player.alimony > 0:
            current_player.alimony -= 1
            tax, property_income = update_income_tax(player)
            alimoney = 0.1 * property_income
            current_player.money -= int(alimoney)
            print(f'You payed ${int(alimoney)} in alimony!')

        print(f"You currently have ${current_player.money} amount of money.")

        for p in queue.players:
            if p.money < 0:
                queue.handle_debt(p)
        queue.rotate()

    print("Game Over!")
    print("Final:")
    for p in queue.players:
        print(f'The winner of this Monopoly game is {p.name}')
    for p in queue.players:
        owned = []
        for x in player.locs:
            owned.append(locations[x]['description'])
        print(f"{p.name} accumulated: ${p.money}")
        print(f"{p.name} owned: {owned}")
    for p in queue.order:
        pos = queue.order.index(p) + 2
        print(f"\n{p.name} is in number {pos} place")
        print(f"{p.name} accumulated: ${p.money}")


players = [
    Player("Enzo"),
    Player("Edwin"),
    Player("Matthew"),
    Player("Bryan"),
    Player("Jayvis")
]

simulate_game(players)
