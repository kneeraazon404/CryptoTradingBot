
# @version=5
# strategy("Ellijah Davis Strategy", overlay=true)

#?#########################        INPUT         ##################

src = input.source(close, "Source")
type= input.bool(true, "Exponential MA")
# EMA's
GRP4 = "EMA INPUT"
len1 = input.int(8, minval=1, title="Length EMA1",group=GRP4)
len2 = input.int(13, minval=1, title="Length EMA2",group=GRP4)
len3 = input.int(21, minval=1, title="Length EMA2",group=GRP4)
len4 = input.int(55, minval=1, title="Length EMA2",group=GRP4)

#  TP - SL (%)
GRP5 = "MANAGE ORDERS"
longProfitPerc1 = input.float(title="Take Profit 1(%)", minval=0.0, step=0.01, defval=2,group=GRP5) / 100
longProfitPerc2 = input.float(title="Take Profit 2(%)", minval=0.0, step=0.01, defval=3,group=GRP5) / 100
longProfitPerc3 = input.float(title="Take Profit 3(%)", minval=0.0, step=0.01, defval=5,group=GRP5) / 100
longStopPerc = input.float(title="Stop Loss %", minval=0.0, step=0.01, defval=10,group=GRP5) / 100



###########################        INDICATORS         ##################


# EMA's
ema1 = type? ta.ema(src, len1): ta.sma(src,len1)
ema2 = type? ta.ema(src, len2): ta.sma(src,len2)
ema3 = type? ta.ema(src, len3): ta.sma(src,len3)
ema4 = type? ta.ema(src, len4): ta.sma(src,len4)


 ############     PLOT INDICATORS          ################

plot(ema1, title="EMA1", color=color.aqua,linewidth=2)
plot(ema2, title="EMA2", color=color.fuchsia,linewidth=2)
plot(ema3, title="EMA3", color=color.orange,linewidth=2)
plot(ema4, title="EMA4", color=color.yellow,linewidth=2)

#  ############        MANAGE ORDER          ################

buy_cond = ta.cross(ema3, ema4) and ema1 > ema2 and ema3 > ema4
sell_cond = ta.cross(ema3, ema4) and ema1 < ema2 and ema3 < ema4


plotshape(buy_cond ? 1 : 0, color=color.new(#00FF00,0), style=shape.arrowup, location=location.belowbar, text="Up", size=size.large)
plotshape(sell_cond ? -1 : 0, color=color.new(#FF0000,0), style=shape.arrowdown, location=location.abovebar, text="Down", size=size.large)

#  calculate the TP - SL prices for buying
longProfit1  = strategy.position_avg_price * (1 + longProfitPerc1)
longProfit2  = strategy.position_avg_price * (1 + longProfitPerc2)
longProfit3  = strategy.position_avg_price * (1 + longProfitPerc3)
longStop  = strategy.position_avg_price * (1 - longStopPerc)


#  calculate the TP - SL prices for selling
shortProfit1  = strategy.position_avg_price * (1 - longProfitPerc1)
shortProfit2  = strategy.position_avg_price * (1 - longProfitPerc2)
shortProfit3  = strategy.position_avg_price * (1 - longProfitPerc3)
shortStop  = strategy.position_avg_price * (1 + longStopPerc)

# logic
if (buy_cond)
	strategy.close_all()
	strategy.entry("buy", strategy.long, comment="buY")
if  (sell_cond)
    strategy.close_all()
	strategy.entry("sell", strategy.short, comment="sell")

# logic-exit
if strategy.position_size>0
    strategy.exit(id="closeLong",stop=longStop, limit=longProfit1)

if strategy.position_size<0
    strategy.exit(id="closeShort",stop=shortStop, limit=shortProfit1)

# Ellijag_Davis_v1.txt
