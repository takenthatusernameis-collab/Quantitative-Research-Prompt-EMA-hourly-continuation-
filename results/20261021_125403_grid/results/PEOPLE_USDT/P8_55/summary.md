# EMA Hourly Continuation — PEOPLE/USDT P8_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -3.0720 |
| sortino_ratio | -1.0973 |
| max_drawdown | 0.7334 |
| cagr | -0.3967 |
| net_avg_win | 59.4117 |
| net_avg_loss | -70.4159 |
| avg_hold_time_bars | 17.4301 |
| exposure | 0.5024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
