# EMA Hourly Continuation — AUCTION/USDT P26_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.5034 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -7.4006 |
| sortino_ratio | -3.0847 |
| max_drawdown | 0.9797 |
| cagr | -0.7816 |
| net_avg_win | 25.2988 |
| net_avg_loss | -40.7898 |
| avg_hold_time_bars | 5.7097 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
