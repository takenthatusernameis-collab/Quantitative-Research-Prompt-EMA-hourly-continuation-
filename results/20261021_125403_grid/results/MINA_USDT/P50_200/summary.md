# EMA Hourly Continuation — MINA/USDT P50_200

**Symbol:** MINA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.8459 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -0.8389 |
| sortino_ratio | -0.2060 |
| max_drawdown | 0.2752 |
| cagr | -0.0927 |
| net_avg_win | 78.7580 |
| net_avg_loss | -99.0064 |
| avg_hold_time_bars | 31.8703 |
| exposure | 0.4245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
