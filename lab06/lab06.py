class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"
        return self.before != self.after
    def report(self):
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg = 'no change'
        if self.changed():
            "*** YOUR CODE HERE ***"
            if self.after > self.before:
                msg = f'increased {self.before}->{self.after}'
            else:
                msg = 'decreased {0}->{1}'.format(self.before, self.after)
        else:
            msg = 'no change'
        return str(self.id) + ': ' + msg

class Account:
    """A bank account that tracks its transaction history.

    >>> a = Account('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = Account('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

#*** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***
    
    def __init__(self, account_holder):
        self.i = 0
        self.balance = 0
        self.transactions = []
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount, add the deposit
        to the transaction history, and return the new balance.
        """
        self.transactions.append(Transaction(self.i, self.balance, self.balance + amount))
        self.i += 1
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount, add the withdraw
        to the transaction history, and return the new balance.
        """

        if amount > self.balance:
            self.transactions.append(Transaction(self.i, self.balance, self.balance))
            self.i += 1
            return 'Insufficient funds'
        
        self.transactions.append(Transaction(self.i, self.balance, self.balance - amount))
        self.i += 1

        self.balance = self.balance - amount
        return self.balance




class email:
    """an email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the Client that sent the email
        recipient_name (str): the name of the recipient (another Client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class server:
    """each server has one instance attribute called Clients that is a
    dictionary from Client names to Client objects.
    """
    def __init__(self):
        self.Clients = {}

    def send(self, email):
        """append the email to the inbox of the Client it is addressed to."""
        self.Clients[email.recipient_name].inbox.append(email)


    def register_Client(self, Client):
        """add a Client to the dictionary of Clients."""
        self.Clients[Client.name] = Client

class Client:
    """a Client has a server, a name (str), and an inbox (list).

    >>> s = server()
    >>> a = Client(s, 'alice')
    >>> b = Client(s, 'bob')
    >>> a.compose('hello, world!', 'bob')
    >>> b.inbox[0].msg
    'hello, world!'
    >>> a.compose('cs 61a rocks!', 'bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'cs 61a rocks!'
    >>> b.inbox[1].sender.name
    'alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_Client(self)

    def compose(self, message, recipient_name):
        """send an email with the given message to the recipient."""
        new_email = email(message, self, recipient_name)
        self.server.send(new_email)


def make_change(amount, coins):
    """return a list of coins that sum to amount, preferring the smallest coins
    available and placing the smallest coins first in the returned list.

    the coins argument is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if amount == 0:
        return []
    
    if not coins:
        return None
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    
    "*** your code here ***"
    if amount >= smallest and coins[smallest] > 0:
        result = make_change(amount - smallest, rest)
        if result is not None:
            return [smallest] + result
    
    new_coins = dict(coins)
    del new_coins[smallest]
    return make_change(amount, new_coins)

def remove_one(coins, coin):
    """remove one coin from a dictionary of coins. return a new dictionary,
    leaving the original dictionary coins unchanged.

    >>> coins = {2: 5, 3: 2, 6: 1}
    >>> remove_one(coins, 2) == {2: 4, 3: 2, 6: 1}
    true
    >>> remove_one(coins, 6) == {2: 5, 3: 2}
    true
    >>> coins == {2: 5, 3: 2, 6: 1} # unchanged
    true
    """
    copy = dict(coins)
    count = copy.pop(coin) - 1  # the coin denomination is removed
    if count:
        copy[coin] = count      # the coin denomination is added back
    return copy

class ChangeMachine:
    """a change machine holds a certain number of coins, initially all pennies.
    the change method adds a single coin of some denomination x and returns a
    list of coins that sums to x. the machine prefers to return the smallest
    coins available. the total value in the machine never changes, and it can
    always make change for any coin (perhaps by returning the coin passed in).

    the coins attribute is a dictionary with keys that are positive integer
    denominations and values that are positive integer coin counts.

    >>> m = ChangeMachine(2)
    >>> m.coins == {1: 2}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.coins == {2: 1}
    True
    >>> m.change(2)
    [2]
    >>> m.coins == {2: 1}
    True
    >>> m.change(3)
    [3]
    >>> m.coins == {2: 1}
    True

    >>> m = ChangeMachine(10) # 10 pennies
    >>> m.coins == {1: 10}
    True
    >>> m.change(5) # takes a nickel & returns 5 pennies
    [1, 1, 1, 1, 1]
    >>> m.coins == {1: 5, 5: 1} # 5 pennies & a nickel remain
    True
    >>> m.change(3)
    [1, 1, 1]
    >>> m.coins == {1: 2, 3: 1, 5: 1}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.change(2) # not enough 1's remaining; return a 2
    [2]
    >>> m.coins == {2: 1, 3: 1, 5: 1}
    True
    >>> m.change(8) # cannot use the 2 to make 8, so use 3 & 5
    [3, 5]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(1) # return the penny passed in (it's the smallest)
    [1]
    >>> m.change(9) # return the 9 passed in (no change possible)
    [9]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(10)
    [2, 8]
    >>> m.coins == {10: 1}
    True

    >>> m = ChangeMachine(9)
    >>> [m.change(k) for k in [2, 2, 3]]
    [[1, 1], [1, 1], [1, 1, 1]]
    >>> m.coins == {1: 2, 2: 2, 3: 1}
    True
    >>> m.change(5) # prefers [1, 1, 3] to [1, 2, 2] (more pennies)
    [1, 1, 3]
    >>> m.change(7)
    [2, 5]
    >>> m.coins == {2: 1, 7: 1}
    True
    """
    def __init__(self, pennies):
        self.coins = {1: pennies}

    def change(self, coin):
        """return change for coin, removing the result from self.coins."""
        "*** your code here ***"
        if coin in self.coins:
            self.coins[coin] += 1
        else:
            self.coins[coin] = 1
        
        change_list = make_change(coin, self.coins.copy())

        for c in change_list:
            self.coins[c] -= 1
            if self.coins[c] == 0:
                del self.coins[c]
        return change_list