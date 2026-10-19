# EMA Hourly Continuation — SHIB/USDT P26_34

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.2444 |
| net_win_rate | 0.3609 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -14.1942 |
| sortino_ratio | -6.8127 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 8.4245 |
| net_avg_loss | -19.4620 |
| avg_hold_time_bars | 1.9492 |
| exposure | 0.0943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
