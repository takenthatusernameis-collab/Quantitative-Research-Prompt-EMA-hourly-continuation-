# EMA Hourly Continuation — BNB/USDT P34_55

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9630 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.3436 |
| sortino_ratio | -0.8004 |
| max_drawdown | 0.6088 |
| cagr | -0.3059 |
| net_avg_win | 46.3064 |
| net_avg_loss | -88.4658 |
| avg_hold_time_bars | 5.7610 |
| exposure | 0.0712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
