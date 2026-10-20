# EMA Hourly Continuation — XPR/USDT P34_50

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.2250 |
| net_win_rate | 0.3350 |
| gross_profit_factor | 0.5787 |
| gross_win_rate | 0.3640 |
| sharpe_ratio | -12.5068 |
| sortino_ratio | -5.1842 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 10.9041 |
| net_avg_loss | -24.4177 |
| avg_hold_time_bars | 3.7884 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
