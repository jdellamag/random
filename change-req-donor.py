###### Change Request Crowd Vote ######
    # Reddit style platform that has categories for petitions to change features that people vote on
        # or instead of platform just a plug-in and website add on tool that lets people contribute to a companies preexisting service ticket feature req voting system
        # not actually associated with the websites but can win with social perspective and reputation
    # link to crypto, keep money in smart contract that pays out the org if the feature gets implemented, but can loan against your pledge
    # could give the companies the option to kyc and have an admin accept or deny the change req, which would then release the contract 
    # this would present the need for some social reputation or 
    # Company can set a price bounty (i.e. 'if we raise X amount, we implement the change')


#### Parts to the tool: ####
    # Website homepage that shows active proposals and summary details
        # Company name, brief summary of proposal, voting timeframe, funds raised, funding goal
        # Need to find some way for the company to accept, deny, mark proposal in progress
    # User submittal button/form for feature request
        # User comments section, up/down votes or just funding contributions - what is more impactful in eyes of company
    # Expaned proposal details page
    # Crypto wallet connector
    # Fiat bank connector
    # Escrow wallet
    # Crypto <==> Fiat converter (TBD)
    # Company registration or claim page (KYC)


### Questions to Answer ###
    # Do you give companies the option to accepts either crypto or fiat, or just allow both?
        # give them the option during corporate setup to choose to collect crypto/fiat at time of donation, or swap crypto donations directly to cash at time of transaction?
    # With cryptos volitility, will companies be willing to let tokens sit in a wallet without cashing in?
        # Means that solution engineers could get paid significantly less, but also more
    # Are donors contributing actual tokens? Bluechips only, shitcoins, etc?
        # Do you allow all token contributions, but just route them through a swap instantaneously?
            # Could either swap directly to bluechip crypto or directly to cash
    # How do you incentivize the companies to make the changes other than money?  IT solution implemmentation takes a long time and can be difficult
        # And how do you confirm the change implemented is exactly as needed? Different parties need differnt things
        # Submissions would likely need to have pretty detailed tech specs, unless you only accepted very simple reqs
    # Because the length of IT solution implementation can be so long, does that support taking crypto donations and swapping to fiat immediately so you are not at the mercy of price cycles
        # But then how do you return the funds to the donor if you swap right away?
    # How do you sync with companies finance department?
    # Do you need some sort of satifaction mechinism for showing how much people like the implemented change?
        # Would help gauge success of the fix



# Base currency prices
usd_price = 1
eth_price = 2400
btc_price = 30000


asset = input("What assest would you like to pledge?\nUSD\nETH\nBTC\n")
amount = int(input("How many will you contribute?\n"))


def btc_usd():
    return(amount * btc_price)
def eth_usd():
    return(amount * eth_price)
def invalid_input():
    return("Invalid currency choice.")

def pledge_amount():
    if asset == "btc" or asset == "BTC":
        return('Your contribution is worth $',btc_usd())
    elif asset == "eth" or asset == "ETH":
        return('Your contribution is worth $',eth_usd())
    elif asset == "usd" or asset == "USD":
        return('Your contribution is worth $',amount)
    else:
        return(invalid_input())


print(pledge_amount())
# print("Your contribution is worth $",pledge_amount(), "!")


# print("Are you sure you want to pledge",amount,asset,"?")
# input("Y/N\n")

