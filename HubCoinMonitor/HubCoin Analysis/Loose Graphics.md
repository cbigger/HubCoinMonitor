***
Total payers to date, PS

Private_Sector.groupby(["From","FromPlayer"]).sum().sort_values(by=["Quantity"],ascending=False)

![[Pasted image 20220706101945.png]]

***
Total earners to date, PS

*Private_Sector.groupby(["To","ToPlayer"]).sum().sort_values(by=["Quantity"],ascending=False)*

![[Pasted image 20220706102034.png]]

***
Bar chart of private sector transactions, not including corvus awards/syn payments
![[Pasted image 20220706101845.png]]

***
Balance vs. SentCoin vs. Total Contribution (May + June) for major accounts (>8000HC)

*AFPS = Accounts.copy()
for x in PublicFunds:
    AFPS.drop(AFPS[AFPS["Address"] == PublicFunds[x]].index, inplace=True)
AFPS.sort_values(by="Balance")
AFCut = AFPS[["Player","Balance","Sent","TotalContribution"]]
AFCut = AFCut[AFCut["Balance"]>800]
AFCut = AFCut[AFCut["Balance"]<100000]
AFCut = AFCut.sort_values(by = "Balance")
AFCut.plot.bar(x="Player",stacked=True,figsize=(40,25),fontsize=26)*

![[Pasted image 20220708140039.png]]

Same thing but fixed a bit and with player names

*AFPS = Accounts.copy()
for x in PublicFunds:
    AFPS.drop(AFPS[AFPS["Address"] == PublicFunds[x]].index, inplace=True)
AFPS.sort_values(by="Balance")
AFCut = AFPS[["Player","Balance","Sent","TotalContribution"]]
AFCut = AFCut[AFCut["Balance"]>1000]
AFCut = AFCut[AFCut["Balance"]<100000]
AFCut = AFCut.sort_values(by = "Balance")
AFCut.plot.bar(x="Player",stacked=True,figsize=(40,25),fontsize=26)*

![[Pasted image 20220708132541.png]]

