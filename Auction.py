import art
import subprocess   
clear = lambda: subprocess.call('cls||clear', shell=True)


print(art.logo)
list = []
def add_list(name,bid):
  
  new_dic = {
    "name": name,
    "bid": bid
  }
  list.append(new_dic)

def declare_winner(list):
  max_bid = 0
  for dic in list:
    if max_bid < int(dic["bid"]):
      max_bid = int(dic["bid"])
      winner = dic["name"]
  print(f"Winner of the auction is (The one who pays the most:D) {winner} with the price ${max_bid}")

while True:  
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  add_list(name, bid)
  while True:
    flag = input("Is there any one who want to bid too?(yes or no)").lower()
    if flag != "yes" and flag != "no":
      print("Invalid input! Let's try again")
      continue
    else:
      break
  if flag == "yes":
    clear()
    continue
  else:
    clear()
    break

declare_winner(list)