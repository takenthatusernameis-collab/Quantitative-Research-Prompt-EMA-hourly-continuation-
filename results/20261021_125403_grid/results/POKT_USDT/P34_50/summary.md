# EMA Hourly Continuation — POKT/USDT P34_50

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.5920 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8398 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -3.3047 |
| sortino_ratio | -0.8489 |
| max_drawdown | 0.6444 |
| cagr | -0.3239 |
| net_avg_win | 63.2077 |
| net_avg_loss | -83.5658 |
| avg_hold_time_bars | 7.3049 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
