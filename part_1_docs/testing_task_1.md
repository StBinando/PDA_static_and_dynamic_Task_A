### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    if card.value = 1:  # single equal symbol "=" is wrong syntax for condition
                        # should be "=="; change to "card.value == 1"
      return True
    else  # missing ":" after "else"
      return False


  dif highest_card(self, card1 card2):  # typo on first word ("dif" instead of "def");
                                        # missing "," after "card1

  # the whole block below lines 21 to 35 should be indented to the righ
  if card1.value > card2.value:
    return card # should return "card1", being the name of the argument passed to the function,
                # and tested in the conditional statement
  else:
    return card2


# lines 39 to 42 should be indented to the righ; line 44 ok
def cards_total(self, cards):
  total   # initialisation of variable "total" should be "total = 0"
  for card in cards:
    total += card.value # as the function should count the cards, we don't need to check 
                        # the actual value of the card. It should be "total += 1"
    return "You have a total of" + total  # add a space after "of" and convert "total" to string for
                                          # concatenation should be "You have a total of " str(total)
  

```
