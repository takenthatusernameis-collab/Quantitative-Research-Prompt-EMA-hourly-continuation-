# EMA Hourly Continuation — BLZ/USDT P34_50

**Symbol:** BLZ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.3611 |
| net_win_rate | 0.3733 |
| gross_profit_factor | 0.7805 |
| gross_win_rate | 0.4046 |
| sharpe_ratio | -10.8836 |
| sortino_ratio | -4.7909 |
| max_drawdown | 0.9977 |
| cagr | -0.9106 |
| net_avg_win | 15.7514 |
| net_avg_loss | -25.9839 |
| avg_hold_time_bars | 3.6413 |
| exposure | 0.1580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
