# EMA Hourly Continuation — PEOPLE/USDT P26_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1033 |
| net_profit_factor | 0.2917 |
| net_win_rate | 0.3998 |
| gross_profit_factor | 0.6184 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -10.4296 |
| sortino_ratio | -4.7670 |
| max_drawdown | 0.9976 |
| cagr | -0.9092 |
| net_avg_win | 9.9494 |
| net_avg_loss | -22.7186 |
| avg_hold_time_bars | 2.2759 |
| exposure | 0.1064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
