# EMA Hourly Continuation — AVAX/USDT P8_34

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -3.0535 |
| sortino_ratio | -1.1454 |
| max_drawdown | 0.7530 |
| cagr | -0.4085 |
| net_avg_win | 57.4340 |
| net_avg_loss | -73.1972 |
| avg_hold_time_bars | 8.9855 |
| exposure | 0.2814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
