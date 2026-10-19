# EMA Hourly Continuation — LUNC/USDT P20_50

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.3151 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.6689 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -9.6107 |
| sortino_ratio | -4.4382 |
| max_drawdown | 0.9960 |
| cagr | -0.8888 |
| net_avg_win | 10.3897 |
| net_avg_loss | -23.3414 |
| avg_hold_time_bars | 4.3741 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
